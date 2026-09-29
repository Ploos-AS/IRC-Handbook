#!/usr/bin/env python3
"""Minimal educational IRC bot using only the Python standard library."""
from __future__ import annotations
import base64, os, random, signal, socket, ssl, time
from dataclasses import dataclass, field

class SessionError(Exception): pass
class AuthenticationError(SessionError): pass
class ServerError(SessionError): pass
class ConnectionClosed(SessionError): pass

@dataclass(frozen=True)
class SessionResult:
    healthy:bool
    stopped:bool=False

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
def _unescape_tag(v):
    out=[];i=0;esc={":":";","s":" ","\\":"\\","r":"\r","n":"\n"}
    while i<len(v):
        if v[i]=="\\":
            i+=1
            if i>=len(v):break
            out.append(esc.get(v[i],v[i]))
        else:
            out.append(v[i])
        i+=1
    return "".join(out)
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
def sasl_authenticate_lines(u,p):
    payload=sasl_plain(u,p);chunks=[payload[i:i+400] for i in range(0,len(payload),400)]
    if len(payload)%400==0:chunks.append("+")
    return ["AUTHENTICATE "+chunk for chunk in chunks]

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

@dataclass
class ServerFeatures:
    values:dict[str,str|bool]=field(default_factory=dict)
    def update(self,m):
        for key,value in parse_isupport(m).items():
            if value is False:self.values.pop(key,None)
            else:self.values[key]=value
    @property
    def casemapping(self):
        value=self.values.get("CASEMAPPING","rfc1459")
        return value if value in {"ascii","rfc1459","strict-rfc1459"} else "rfc1459"
    @property
    def prefix(self):
        parsed=parse_prefix(self.values.get("PREFIX","(ov)@+"))
        return parsed or {"o":"@","v":"+"}
    @property
    def chanmodes(self):
        parsed=parse_chanmodes(self.values.get("CHANMODES","beI,k,l,imnst"))
        return parsed or ("beI","k","l","imnst")
    @property
    def chantypes(self):
        value=self.values.get("CHANTYPES","#&")
        return value if isinstance(value,str) and value else "#&"

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
        self.names_active=False;self.names_seen=set();self.names_pending={};self.names_events=[]
    def key(self,nick):return irc_casefold(nick,self.casemapping)
    def add_member(self,nick,modes=()):
        member=self.members.setdefault(self.key(nick),Member(nick,set()));member.modes.update(modes);return member
    def begin_names(self):
        if not self.names_active:
            self.names_active=True;self.names_seen=set();self.names_pending={};self.names_events=[]
    def end_names(self):
        if self.names_active:
            self.members={k:Member(v.nick,set(v.modes)) for k,v in self.names_pending.items()}
            events=self.names_events
            self.names_active=False;self.names_seen=set();self.names_pending={};self.names_events=[]
            for event,prefix_map in events:self.apply(event,prefix_map)
    def add_names(self,text,prefix_map=None):
        self.begin_names()
        prefix_map=prefix_map or {m:p for m,p in zip(self.prefix_modes,"@+"[:len(self.prefix_modes)])}
        by_prefix={p:m for m,p in prefix_map.items()}
        for token in text.split():
            modes=set()
            while token and token[0] in by_prefix:modes.add(by_prefix[token[0]]);token=token[1:]
            if token:
                key=self.key(token);member=self.names_pending.setdefault(key,Member(token,set()));member.modes.update(modes);self.names_seen.add(key)
    def configure(self,features):
        old_members=list(self.members.values());old_seen=set(self.names_seen)
        self.casemapping=features.casemapping;self.prefix_modes="".join(features.prefix);self.chanmodes=features.chanmodes
        rebuilt={}
        for member in old_members:
            key=self.key(member.nick)
            if key in rebuilt:
                rebuilt[key].modes.update(member.modes)
            else:
                rebuilt[key]=Member(member.nick,set(member.modes))
        self.members=rebuilt
        if self.names_active:
            pending=list(self.names_pending.values())
            self.names_pending={}
            for member in pending:
                key=self.key(member.nick)
                if key in self.names_pending:self.names_pending[key].modes.update(member.modes)
                else:self.names_pending[key]=Member(member.nick,set(member.modes))
            self.names_seen=set(self.names_pending)
        self.lists={m:self.lists.get(m,set()) for m in self.chanmodes[0]}
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
    def apply(self,m,prefix_map=None):
        sender=m.prefix.split("!",1)[0] if m.prefix else None
        if m.command=="353" and len(m.params)>=4 and irc_equal(m.params[2],self.name,self.casemapping):
            self.add_names(m.params[3],prefix_map);return
        if m.command=="366" and len(m.params)>=2 and irc_equal(m.params[1],self.name,self.casemapping):self.end_names();return
        if self.names_active and m.command not in {"353","366"}:
            self.names_events.append((m,prefix_map));return
        if m.command=="JOIN" and sender and m.params and irc_equal(m.params[0],self.name,self.casemapping):
            self.add_member(sender)
        elif m.command=="PART" and sender and m.params and irc_equal(m.params[0],self.name,self.casemapping):self.remove_member(sender)
        elif m.command=="KICK" and len(m.params)>=2 and irc_equal(m.params[0],self.name,self.casemapping):self.remove_member(m.params[1])
        elif m.command=="QUIT" and sender:self.remove_member(sender)
        elif m.command=="NICK" and sender and m.params:self.rename_member(sender,m.params[0])
        elif m.command=="MODE" and len(m.params)>=2 and irc_equal(m.params[0],self.name,self.casemapping):self.apply_mode(m.params[1],m.params[2:])

class ChannelRegistry:
    """Route channel events to independent ChannelState instances."""
    def __init__(self,features,own_nick=None):
        self.features=features;self.own_nick=own_nick;self.channels={}
    def is_own(self,nick):
        return self.own_nick is not None and irc_equal(nick,self.own_nick,self.features.casemapping)
    def discard(self,name):
        self.channels.pop(self.key(name),None)
    def reset(self):
        self.channels.clear()
    def key(self,name):return irc_casefold(name,self.features.casemapping)
    def get(self,name):
        key=self.key(name)
        if key not in self.channels:
            self.channels[key]=ChannelState(name);self.channels[key].configure(self.features)
        return self.channels[key]
    def reconfigure(self):
        old=list(self.channels.values());self.channels={}
        for state in old:
            state.configure(self.features);self.channels[self.key(state.name)]=state
    def apply(self,m):
        sender=m.prefix.split("!",1)[0] if m.prefix else None
        if m.command=="JOIN" and sender and m.params and self.is_own(sender):
            self.get(m.params[0]).apply(m,self.features.prefix);return
        if m.command=="PART" and sender and m.params and self.is_own(sender):
            self.discard(m.params[0]);return
        if m.command=="KICK" and len(m.params)>=2 and self.is_own(m.params[1]):
            self.discard(m.params[0]);return
        if m.command=="NICK" and sender and m.params and self.is_own(sender):
            self.own_nick=m.params[0]
        if m.command=="353" and len(m.params)>=4:self.get(m.params[2]).apply(m,self.features.prefix);return
        if m.command=="366" and len(m.params)>=2:self.get(m.params[1]).apply(m,self.features.prefix);return
        if m.command in {"JOIN","PART"} and m.params:self.get(m.params[0]).apply(m,self.features.prefix);return
        if m.command=="KICK" and m.params:self.get(m.params[0]).apply(m,self.features.prefix);return
        if m.command=="MODE" and m.params and m.params[0] and m.params[0][0] in self.features.chantypes:self.get(m.params[0]).apply(m,self.features.prefix);return
        if m.command in {"QUIT","NICK"}:
            for state in self.channels.values():state.apply(m,self.features.prefix)

@dataclass
class SessionState:
    initial_nick:str
    features:ServerFeatures=field(default_factory=ServerFeatures)
    channels:ChannelRegistry=field(init=False)
    healthy:bool=False
    def __post_init__(self):
        self.channels=ChannelRegistry(self.features,self.initial_nick)
    @property
    def nick(self):return self.channels.own_nick
    def apply(self,m):
        if m.command=="001":
            self.healthy=True
            if m.params:self.channels.own_nick=m.params[0]
        if m.command=="005":
            self.features.update(m);self.channels.reconfigure()
        self.channels.apply(m)

def channel_snapshot(state):
    return {"name":state.name,"casemapping":state.casemapping,
     "members":{k:{"nick":m.nick,"modes":sorted(m.modes)} for k,m in sorted(state.members.items())},
     "modes":sorted(state.modes),"mode_values":dict(sorted(state.mode_values.items())),
     "lists":{k:sorted(v) for k,v in sorted(state.lists.items())},"names_active":state.names_active}

def registry_snapshot(registry):
    return {k:channel_snapshot(v) for k,v in sorted(registry.channels.items())}

def snapshot_diff(before,after):
    before_keys=set(before);after_keys=set(after)
    return {"added":sorted(after_keys-before_keys),"removed":sorted(before_keys-after_keys),
     "changed":sorted(k for k in before_keys&after_keys if before[k]!=after[k])}

def assert_registry_invariants(registry):
    for key,state in registry.channels.items():
        if key!=registry.key(state.name):raise AssertionError("channel registry key mismatch")
        for member_key,member in state.members.items():
            if member_key!=state.key(member.nick):raise AssertionError("member key mismatch")
            if not member.modes.issubset(set(state.prefix_modes)):raise AssertionError("unknown member prefix mode")
    return True

def mutate_transcript(lines,seed=0,rounds=32):
    """Yield deterministic parser/state mutations suitable for repeatable fuzz tests."""
    rng=random.Random(seed);base=list(lines)
    for _ in range(rounds):
        candidate=base.copy()
        if candidate:
            op=rng.randrange(4);i=rng.randrange(len(candidate))
            if op==0:candidate[i]=candidate[i].swapcase()
            elif op==1:candidate.insert(i,candidate[i])
            elif op==2:candidate[i]=candidate[i]+" "
            else:candidate[i]=candidate[i].replace("Alice","ALICE")
        yield candidate

def replay_transcript(lines,features=None,check_invariants=True):
    features=features or ServerFeatures();registry=ChannelRegistry(features)
    for line in lines:
        m=parse_message(line)
        if m.command=="005":features.update(m);registry.reconfigure()
        registry.apply(m)
        if check_invariants:assert_registry_invariants(registry)
    return registry

CTCP_DELIM="\x01"

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

def ctcp_reply(m,nick,case_mapping="rfc1459"):
    """Reply only to direct PRIVMSG CTCP queries; never reply to NOTICE or channel CTCP."""
    if m.command!="PRIVMSG" or len(m.params)<2 or not m.prefix or not irc_equal(m.params[0],nick,case_mapping):return []
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

class Registration:
    """Explicit registration phases for one IRC connection."""
    def __init__(self,nick,channel,use_sasl=False,sasl_required=False):
        self.requested_nick=nick;self.channel=channel
        self.negotiation=Negotiation(use_sasl,sasl_required)
        self.phase="new";self.join_sent=False
    @property
    def registered(self):return self.phase=="registered"
    def start(self):
        if self.phase!="new":return []
        self.phase="cap";return ["CAP LS 302",f"NICK {self.requested_nick}",f"USER {self.requested_nick} 0 * :IRC Handbook Bot"]
    def actions(self,m,current_nick,sasl_user=None,sasl_password=None,case_mapping="rfc1459"):
        if m.command=="ERROR":raise ServerError(m.params[-1] if m.params else "IRC server error")
        if m.command=="PING" and m.params:return ["PONG :"+m.params[-1]]
        if m.command=="433":
            self.phase="registering";return [f"NICK {current_nick}_"]
        if m.command=="CAP":
            if self.registered:return []
            out=self.negotiation.actions(m)
            if any(x=="AUTHENTICATE PLAIN" for x in out):self.phase="sasl"
            elif any(x=="CAP END" for x in out):self.phase="registering"
            return out
        if m.command=="AUTHENTICATE" and m.params==["+"] and self.phase=="sasl" and sasl_user is not None and sasl_password is not None:
            return sasl_authenticate_lines(sasl_user,sasl_password)
        if m.command=="903":
            if self.phase!="sasl":return []
            self.phase="registering";return ["CAP END"]
        if m.command in {"904","905","906","907"} and sasl_user is not None:
            if self.phase!="sasl":return []
            if self.negotiation.sasl_required:raise AuthenticationError("SASL authentication failed")
            self.phase="registering";return ["CAP END"]
        if m.command=="001":
            self.phase="registered"
            if not self.join_sent:
                self.join_sent=True;return [f"JOIN {self.channel}"]
        return []

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

def actions_for_message(m,nick,channel,sasl_user=None,sasl_password=None,sasl_required=False,case_mapping="rfc1459"):
    if m.command=="ERROR":raise ServerError(m.params[-1] if m.params else "IRC server error")
    if m.command=="PING" and m.params:return ["PONG :"+m.params[-1]]
    ctcp=ctcp_reply(m,nick,case_mapping)
    if ctcp:return ctcp
    if m.command=="PRIVMSG" and len(m.params)>=2 and m.prefix:
        sender=m.prefix.split("!",1)[0];target,text=m.params[0],m.params[1]
        if parse_ctcp(text):return []
        if text.strip()=="!hello":return [f"PRIVMSG {sender if irc_equal(target,nick,case_mapping) else target} :Hello, {sender}!"]
    return []
def response_for_line(line,nick,channel,sasl_user=None,sasl_password=None,sasl_required=False,negotiation=None):
    try:m=parse_message(line)
    except ValueError:return []
    if m.command=="CAP":
        if negotiation is None:return []
        return negotiation.actions(m)
    return actions_for_message(m,nick,channel,sasl_user,sasl_password,sasl_required)
def iter_lines(sock,stop=None,poll_timeout=.5):
    """Yield IRC lines while periodically returning control for shutdown checks."""
    buf=b"";sock.settimeout(poll_timeout)
    while not (stop and stop.requested):
        try:chunk=sock.recv(4096)
        except socket.timeout:continue
        if not chunk:return
        buf+=chunk
        while b"\n" in buf:
            raw,buf=buf.split(b"\n",1);yield raw.rstrip(b"\r").decode("utf-8",errors="replace")
def connect(c):
    raw=socket.create_connection((c.host,c.port),timeout=30)
    return raw if not c.use_tls else ssl.create_default_context().wrap_socket(raw,server_hostname=c.host)
def run_session(c,stop=None):
    stop=stop or StopFlag();registration=Registration(c.nick,c.channel,c.use_sasl,c.sasl_required);session=SessionState(c.nick)
    with connect(c) as sock:
        for line in registration.start():sock.sendall(encode_line(line))
        for line in iter_lines(sock,stop):
            if stop.requested:break
            print(f"<< {line}")
            try:m=parse_message(line)
            except ValueError:continue
            session.apply(m)
            registration_responses=registration.actions(m,session.nick,c.sasl_user,c.sasl_password,session.features.casemapping)
            responses=registration_responses or actions_for_message(m,session.nick,c.channel,None,None,False,session.features.casemapping)
            for response in responses:
                shown="AUTHENTICATE <redacted>" if response.startswith("AUTHENTICATE ") and response!="AUTHENTICATE PLAIN" else response
                print(f">> {shown}");sock.sendall(encode_line(response))
        if stop.requested:
            try:sock.sendall(encode_line("QUIT :Shutting down"))
            except OSError:pass
            return SessionResult(session.healthy,True)
        raise ConnectionClosed("IRC server closed the connection")
def validate(c):
    if (c.sasl_user is None)!=(c.sasl_password is None):raise SystemExit("set both IRC_SASL_USER and IRC_SASL_PASSWORD")
    if c.sasl_required and not c.use_sasl:raise SystemExit("IRC_SASL_REQUIRED needs SASL credentials")
    if c.use_sasl and not c.use_tls:raise SystemExit("SASL PLAIN requires TLS")
def main():
    c=Config.from_env();validate(c);stop=StopFlag()
    signal.signal(signal.SIGINT,stop.request);signal.signal(signal.SIGTERM,stop.request)
    backoff=Backoff()
    while not stop.requested:
        try:
            result=run_session(c,stop)
            if result.healthy:backoff.reset()
        except AuthenticationError as e:raise SystemExit(f"authentication policy failed: {e}")
        except (OSError,ssl.SSLError,SessionError) as e:print(f"session error: {e}")
        if stop.requested:break
        delay=backoff.next_delay();print(f"reconnecting in {delay:g}s")
        # sleep in short intervals so SIGINT/SIGTERM can stop reconnect promptly
        end=time.monotonic()+delay
        while not stop.requested and time.monotonic()<end:time.sleep(min(.25,end-time.monotonic()))
if __name__=="__main__":main()
