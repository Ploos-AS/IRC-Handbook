#!/usr/bin/env python3
"""Minimal educational IRC bot using only the Python standard library."""
from __future__ import annotations
import base64, os, signal, socket, ssl, time
from dataclasses import dataclass

class SessionError(Exception): pass
class AuthenticationError(SessionError): pass
class ServerError(SessionError): pass

@dataclass(frozen=True)
class Message:
    tags:dict[str,str|None]; prefix:str|None; command:str; params:list[str]
@dataclass(frozen=True)
class Config:
    host:str;port:int;nick:str;channel:str;use_tls:bool=True
    sasl_user:str|None=None;sasl_password:str|None=None;sasl_required:bool=False
    @classmethod
    def from_env(cls):
        return cls(os.environ.get("IRC_HOST","irc.example.net"),int(os.environ.get("IRC_PORT","6697")),
         os.environ.get("IRC_NICK","handbookbot"),os.environ.get("IRC_CHANNEL","#handbook-test"),
         os.environ.get("IRC_TLS","1")!="0",os.environ.get("IRC_SASL_USER"),os.environ.get("IRC_SASL_PASSWORD"),
         os.environ.get("IRC_SASL_REQUIRED","0")=="1")
    @property
    def use_sasl(self):return self.sasl_user is not None and self.sasl_password is not None
@dataclass
class Backoff:
    initial:float=2.0;maximum:float=60.0;factor:float=2.0;attempt:int=0
    def next_delay(self):
        delay=min(self.initial*(self.factor**self.attempt),self.maximum);self.attempt+=1;return delay
    def reset(self):self.attempt=0

class StopFlag:
    def __init__(self):self.requested=False
    def request(self,*_):self.requested=True

def encode_line(line):
    if "\r" in line or "\n" in line:raise ValueError("IRC lines must not contain CR or LF")
    return (line+"\r\n").encode()
def _unescape_tag(v):return v.replace(r"\:",";").replace(r"\s"," ").replace(r"\\","\\").replace(r"\r","\r").replace(r"\n","\n")
def parse_message(line):
    tags={};prefix=None;rest=line
    if rest.startswith("@"):
        raw,sep,rest=rest.partition(" ")
        if not sep:raise ValueError("tags without command")
        for item in raw[1:].split(";"):
            k,eq,v=item.partition("=");tags[k]=_unescape_tag(v) if eq else None
    if rest.startswith(":"):
        prefix,sep,rest=rest[1:].partition(" ")
        if not sep:raise ValueError("prefix without command")
    command,sep,rest=rest.partition(" ")
    if not command:raise ValueError("missing command")
    params=[]
    while sep and rest:
        if rest.startswith(":"):params.append(rest[1:]);break
        p,sep,rest=rest.partition(" ");params.append(p)
        while sep and rest.startswith(" "):rest=rest[1:]
    return Message(tags,prefix,command.upper(),params)
def parse_privmsg(line):
    try:m=parse_message(line)
    except ValueError:return None
    if m.command!="PRIVMSG" or len(m.params)<2 or not m.prefix:return None
    return m.prefix.split("!",1)[0],m.params[0],m.params[1]
def sasl_plain(u,p):return base64.b64encode(("\0"+u+"\0"+p).encode()).decode("ascii")

def parse_isupport(m):
    """Parse useful 005 RPL_ISUPPORT tokens into a small feature dictionary."""
    if m.command!="005" or len(m.params)<2:return {}
    out={}
    # params[0] is our nick; the final human-readable parameter is not a token.
    for token in m.params[1:-1]:
        if token.startswith("-"):
            out[token[1:]]=False
        else:
            key,eq,value=token.partition("=")
            out[key]=value if eq else True
    return out

def is_numeric(m):
    return len(m.command)==3 and m.command.isdigit()

def parse_prefix(value):
    """Return {mode: prefix}, e.g. PREFIX=(ov)@+ -> {'o':'@','v':'+'}."""
    if not isinstance(value,str) or not value.startswith("(") or ")" not in value:return {}
    modes,prefixes=value[1:].split(")",1)
    if len(modes)!=len(prefixes):return {}
    return dict(zip(modes,prefixes))

def parse_chanmodes(value):
    """Split CHANMODES=A,B,C,D into its four mode classes."""
    if not isinstance(value,str):return ()
    groups=value.split(",")
    return tuple(groups) if len(groups)==4 else ()

def irc_casefold(value,mapping="rfc1459"):
    """Case-fold IRC identifiers according to CASEMAPPING."""
    folded=value.lower()
    if mapping=="ascii":return folded
    table=str.maketrans({"[":"{","]":"}","\\":"|"})
    folded=folded.translate(table)
    if mapping=="rfc1459":folded=folded.replace("^","~")
    elif mapping!="strict-rfc1459":raise ValueError("unsupported CASEMAPPING")
    return folded

def irc_equal(a,b,mapping="rfc1459"):
    return irc_casefold(a,mapping)==irc_casefold(b,mapping)

@dataclass(frozen=True)
class ModeChange:
    adding:bool; mode:str; parameter:str|None=None

def parse_mode_changes(mode_string,parameters=(),prefix_modes="",chanmodes=()):
    """Parse a MODE string using PREFIX modes and CHANMODES parameter rules."""
    groups=chanmodes if len(chanmodes)==4 else ("","","","")
    always=set(groups[0]+groups[1]+prefix_modes)
    set_only=set(groups[2])
    params=iter(parameters); adding=True; out=[]
    for ch in mode_string:
        if ch=="+":adding=True;continue
        if ch=="-":adding=False;continue
        needs_param=ch in always or (adding and ch in set_only)
        parameter=next(params,None) if needs_param else None
        if needs_param and parameter is None:raise ValueError(f"MODE {ch} requires a parameter")
        out.append(ModeChange(adding,ch,parameter))
    try:next(params)
    except StopIteration:return out
    raise ValueError("unused MODE parameters")

@dataclass
class Member:
    nick:str
    modes:set[str]

class ChannelState:
    """Small replayable model of one IRC channel."""
    def __init__(self,name,casemapping="rfc1459",prefix_modes="ov",chanmodes=("beI","k","l","imnst")):
        self.name=name;self.casemapping=casemapping;self.prefix_modes=prefix_modes;self.chanmodes=chanmodes
        self.members={};self.modes=set();self.mode_values={};self.lists={m:set() for m in chanmodes[0]}
    def key(self,nick):return irc_casefold(nick,self.casemapping)
    def add_member(self,nick):self.members.setdefault(self.key(nick),Member(nick,set()))
    def remove_member(self,nick):self.members.pop(self.key(nick),None)
    def rename_member(self,old,new):
        member=self.members.pop(self.key(old),None)
        if member:self.members[self.key(new)]=Member(new,member.modes)
    def apply_mode(self,mode_string,parameters=()):
        for change in parse_mode_changes(mode_string,parameters,self.prefix_modes,self.chanmodes):
            if change.mode in self.prefix_modes:
                member=self.members.get(self.key(change.parameter))
                if member:
                    (member.modes.add if change.adding else member.modes.discard)(change.mode)
            elif change.mode in self.chanmodes[0]:
                values=self.lists.setdefault(change.mode,set())
                (values.add if change.adding else values.discard)(change.parameter)
            elif change.mode in self.chanmodes[1]+self.chanmodes[2]:
                if change.adding:
                    self.modes.add(change.mode);self.mode_values[change.mode]=change.parameter
                else:
                    self.modes.discard(change.mode);self.mode_values.pop(change.mode,None)
            else:
                (self.modes.add if change.adding else self.modes.discard)(change.mode)
    def apply(self,m):
        sender=m.prefix.split("!",1)[0] if m.prefix else None
        if m.command=="JOIN" and sender and m.params and irc_equal(m.params[0],self.name,self.casemapping):self.add_member(sender)
        elif m.command=="PART" and sender and m.params and irc_equal(m.params[0],self.name,self.casemapping):self.remove_member(sender)
        elif m.command=="KICK" and len(m.params)>=2 and irc_equal(m.params[0],self.name,self.casemapping):self.remove_member(m.params[1])
        elif m.command=="QUIT" and sender:self.remove_member(sender)
        elif m.command=="NICK" and sender and m.params:self.rename_member(sender,m.params[0])
        elif m.command=="MODE" and len(m.params)>=2 and irc_equal(m.params[0],self.name,self.casemapping):self.apply_mode(m.params[1],m.params[2:])

CTCP_DELIM="\\x01"

@dataclass(frozen=True)
class CtcpMessage:
    command:str
    argument:str|None=None

def parse_ctcp(text):
    """Parse one complete CTCP frame; ordinary text returns None."""
    if len(text)<2 or not (text.startswith(CTCP_DELIM) and text.endswith(CTCP_DELIM)):return None
    body=text[1:-1]
    if not body:return None
    command,sep,argument=body.partition(" ")
    return CtcpMessage(command.upper(),argument if sep else None)

def ctcp_frame(command,argument=None):
    if "\\r" in command or "\\n" in command or CTCP_DELIM in command:raise ValueError("invalid CTCP command")
    if argument is not None and ("\\r" in argument or "\\n" in argument or CTCP_DELIM in argument):raise ValueError("invalid CTCP argument")
    return CTCP_DELIM+command+((" "+argument) if argument is not None else "")+CTCP_DELIM

def ctcp_reply(m,nick):
    """Reply only to direct PRIVMSG CTCP queries; never reply to NOTICE or channel CTCP."""
    if m.command!="PRIVMSG" or len(m.params)<2 or not m.prefix or not irc_equal(m.params[0],nick):return []
    request=parse_ctcp(m.params[1])
    if not request or request.command=="ACTION":return []
    sender=m.prefix.split("!",1)[0]
    if request.command=="VERSION":return [f"NOTICE {sender} :"+ctcp_frame("VERSION","IRC Handbook educational bot")]
    if request.command=="PING" and request.argument is not None:return [f"NOTICE {sender} :"+ctcp_frame("PING",request.argument)]
    if request.command=="TIME":return [f"NOTICE {sender} :"+ctcp_frame("TIME","not exposed by educational bot")]
    return []

def parse_capabilities(text):
    """Parse a CAP capability list into {name: value|None}."""
    out={}
    for token in text.split():
        name,eq,value=token.partition("=")
        out[name]=value if eq else None
    return out

class CapabilityState:
    """Track advertised and enabled IRCv3 capabilities."""
    def __init__(self):self.available={};self.enabled=set();self._ls_pending={}
    def apply(self,m):
        if m.command!="CAP" or len(m.params)<2:return
        sub=m.params[1].upper()
        if sub=="LS":
            continuation=len(m.params)>=3 and m.params[-2]=="*"
            self._ls_pending.update(parse_capabilities(m.params[-1]))
            if not continuation:self.available.update(self._ls_pending);self._ls_pending.clear()
        elif sub=="NEW":
            self.available.update(parse_capabilities(m.params[-1]))
        elif sub=="DEL":
            for name in parse_capabilities(m.params[-1]):
                self.available.pop(name,None);self.enabled.discard(name)
        elif sub=="ACK":
            for name in parse_capabilities(m.params[-1]):
                if name.startswith("-"):self.enabled.discard(name[1:])
                else:self.enabled.add(name)

def message_metadata(m):
    """Expose common IRCv3 message tags without requiring them."""
    return {k:m.tags.get(k) for k in ("time","account","msgid","batch") if k in m.tags}

DESIRED_CAPS=("server-time","account-tag","message-tags")

class Negotiation:
    """Stateful CAP negotiation for one connection."""
    def __init__(self,use_sasl=False,sasl_required=False):
        self.caps=CapabilityState();self.use_sasl=use_sasl;self.sasl_required=sasl_required
    def actions(self,m):
        if m.command!="CAP" or len(m.params)<2:return []
        sub=m.params[1].upper();self.caps.apply(m)
        if sub=="LS":
            continuation=len(m.params)>=3 and m.params[-2]=="*"
            if continuation:return []
            wanted=[c for c in DESIRED_CAPS if c in self.caps.available]
            if self.use_sasl:
                if "sasl" in self.caps.available:wanted.append("sasl")
                elif self.sasl_required:raise AuthenticationError("server does not advertise SASL")
            return [("CAP REQ :"+ " ".join(wanted))] if wanted else ["CAP END"]
        if sub=="ACK":
            acknowledged=parse_capabilities(m.params[-1])
            if self.use_sasl and "sasl" in acknowledged:return ["AUTHENTICATE PLAIN"]
            return ["CAP END"]
        if sub=="NAK":
            rejected=parse_capabilities(m.params[-1])
            if self.sasl_required and "sasl" in rejected:raise AuthenticationError("server rejected SASL capability")
            return ["CAP END"]
        return []

def actions_for_message(m,nick,channel,sasl_user=None,sasl_password=None,sasl_required=False):
    use_sasl=sasl_user is not None and sasl_password is not None
    if m.command=="ERROR":raise ServerError(m.params[-1] if m.params else "IRC server error")
    if m.command=="433":return [f"NICK {nick}_"]
    if m.command=="PING" and m.params:return ["PONG :"+m.params[-1]]
    if use_sasl and m.command=="CAP" and len(m.params)>=2:
        sub=m.params[-2] if len(m.params)>=3 else m.params[1];caps=m.params[-1].split()
        if sub=="LS":
            if "sasl" in caps:return ["CAP REQ :sasl"]
            if sasl_required:raise AuthenticationError("server does not advertise SASL")
            return ["CAP END"]
        if sub=="ACK" and "sasl" in caps:return ["AUTHENTICATE PLAIN"]
        if sub=="NAK":
            if sasl_required:raise AuthenticationError("server rejected SASL capability")
            return ["CAP END"]
    if use_sasl and m.command=="AUTHENTICATE" and m.params==["+"]:return ["AUTHENTICATE "+sasl_plain(sasl_user,sasl_password)]
    if use_sasl and m.command=="903":return ["CAP END"]
    if use_sasl and m.command in {"904","905","906","907"}:
        if sasl_required:raise AuthenticationError("SASL authentication failed")
        return ["CAP END"]
    if m.command=="001":return [f"JOIN {channel}"]
    ctcp=ctcp_reply(m,nick)
    if ctcp:return ctcp
    if m.command=="PRIVMSG" and len(m.params)>=2 and m.prefix:
        sender=m.prefix.split("!",1)[0];target,text=m.params[0],m.params[1]
        if parse_ctcp(text):return []
        if text.strip()=="!hello":return [f"PRIVMSG {sender if irc_equal(target,nick) else target} :Hello, {sender}!"]
    return []
def response_for_line(line,nick,channel,sasl_user=None,sasl_password=None,sasl_required=False):
    try:m=parse_message(line)
    except ValueError:return []
    return actions_for_message(m,nick,channel,sasl_user,sasl_password,sasl_required)
def iter_lines(sock):
    buf=b""
    while True:
        chunk=sock.recv(4096)
        if not chunk:return
        buf+=chunk
        while b"\n" in buf:
            raw,buf=buf.split(b"\n",1);yield raw.rstrip(b"\r").decode("utf-8",errors="replace")
def connect(c):
    raw=socket.create_connection((c.host,c.port),timeout=30)
    return raw if not c.use_tls else ssl.create_default_context().wrap_socket(raw,server_hostname=c.host)
def run_session(c,stop=None):
    stop=stop or StopFlag();negotiation=Negotiation(c.use_sasl,c.sasl_required)
    with connect(c) as sock:
        sock.sendall(encode_line("CAP LS 302"))
        sock.sendall(encode_line(f"NICK {c.nick}"));sock.sendall(encode_line(f"USER {c.nick} 0 * :IRC Handbook Bot"))
        for line in iter_lines(sock):
            if stop.requested:
                sock.sendall(encode_line("QUIT :Shutting down"));return
            print(f"<< {line}")
            try:m=parse_message(line)
            except ValueError:continue
            negotiated=negotiation.actions(m)
            responses=negotiated if m.command=="CAP" else actions_for_message(m,c.nick,c.channel,c.sasl_user,c.sasl_password,c.sasl_required)
            for response in responses:
                print(f">> {response}");sock.sendall(encode_line(response))
def validate(c):
    if (c.sasl_user is None)!=(c.sasl_password is None):raise SystemExit("set both IRC_SASL_USER and IRC_SASL_PASSWORD")
    if c.sasl_required and not c.use_sasl:raise SystemExit("IRC_SASL_REQUIRED needs SASL credentials")
def main():
    c=Config.from_env();validate(c);stop=StopFlag()
    signal.signal(signal.SIGINT,stop.request);signal.signal(signal.SIGTERM,stop.request)
    backoff=Backoff()
    while not stop.requested:
        try:run_session(c,stop);backoff.reset()
        except AuthenticationError as e:raise SystemExit(f"authentication policy failed: {e}")
        except (OSError,ssl.SSLError,ServerError) as e:print(f"session error: {e}")
        if stop.requested:break
        delay=backoff.next_delay();print(f"reconnecting in {delay:g}s")
        # sleep in short intervals so SIGINT/SIGTERM can stop reconnect promptly
        end=time.monotonic()+delay
        while not stop.requested and time.monotonic()<end:time.sleep(min(.25,end-time.monotonic()))
if __name__=="__main__":main()
