#!/usr/bin/env python3
"""Minimal educational IRC bot using only the Python standard library."""
from __future__ import annotations
import base64, os, socket, ssl, time
from dataclasses import dataclass

@dataclass(frozen=True)
class Message:
    tags: dict[str, str | None]
    prefix: str | None
    command: str
    params: list[str]

@dataclass(frozen=True)
class Config:
    host: str; port: int; nick: str; channel: str
    use_tls: bool = True
    sasl_user: str | None = None; sasl_password: str | None = None
    @classmethod
    def from_env(cls):
        return cls(os.environ.get("IRC_HOST","irc.example.net"),int(os.environ.get("IRC_PORT","6697")),
                   os.environ.get("IRC_NICK","handbookbot"),os.environ.get("IRC_CHANNEL","#handbook-test"),
                   os.environ.get("IRC_TLS","1")!="0",os.environ.get("IRC_SASL_USER"),os.environ.get("IRC_SASL_PASSWORD"))
    @property
    def use_sasl(self): return self.sasl_user is not None and self.sasl_password is not None

def encode_line(line):
    if "\r" in line or "\n" in line: raise ValueError("IRC lines must not contain CR or LF")
    return (line+"\r\n").encode()

def _unescape_tag(v):
    return v.replace(r"\:", ";").replace(r"\s"," ").replace(r"\\","\\").replace(r"\r","\r").replace(r"\n","\n")

def parse_message(line):
    tags={}; prefix=None; rest=line
    if rest.startswith("@"):
        raw,sep,rest=rest.partition(" ")
        if not sep: raise ValueError("tags without command")
        for item in raw[1:].split(";"):
            k,eq,v=item.partition("="); tags[k]=_unescape_tag(v) if eq else None
    if rest.startswith(":"):
        prefix,sep,rest=rest[1:].partition(" ")
        if not sep: raise ValueError("prefix without command")
    command,sep,rest=rest.partition(" ")
    if not command: raise ValueError("missing command")
    params=[]
    while sep and rest:
        if rest.startswith(":"):
            params.append(rest[1:]); break
        p,sep,rest=rest.partition(" "); params.append(p)
        while sep and rest.startswith(" "): rest=rest[1:]
    return Message(tags,prefix,command.upper(),params)

def parse_privmsg(line):
    try: m=parse_message(line)
    except ValueError: return None
    if m.command!="PRIVMSG" or len(m.params)<2 or not m.prefix: return None
    return m.prefix.split("!",1)[0],m.params[0],m.params[1]

def sasl_plain(user,password):
    return base64.b64encode(("\0"+user+"\0"+password).encode()).decode("ascii")

def response_for_line(line,nick,channel,sasl_user=None,sasl_password=None):
    try: m=parse_message(line)
    except ValueError: return []
    use_sasl=sasl_user is not None and sasl_password is not None
    if m.command=="PING" and m.params: return ["PONG :"+m.params[-1]]
    if use_sasl and m.command=="CAP" and len(m.params)>=2:
        sub=m.params[-2] if len(m.params)>=3 else m.params[1]
        caps=m.params[-1].split()
        if sub=="LS":
            if "sasl" in caps: return ["CAP REQ :sasl"]
            return ["CAP END"]
        if sub=="ACK" and "sasl" in caps: return ["AUTHENTICATE PLAIN"]
        if sub=="NAK": return ["CAP END"]
    if use_sasl and m.command=="AUTHENTICATE" and m.params==["+"]:
        return ["AUTHENTICATE "+sasl_plain(sasl_user,sasl_password)]
    if use_sasl and m.command=="903": return ["CAP END"]
    if use_sasl and m.command in {"904","905","906","907"}: return ["CAP END"]
    if m.command=="001": return [f"JOIN {channel}"]
    if m.command=="PRIVMSG" and len(m.params)>=2 and m.prefix:
        sender=m.prefix.split("!",1)[0]; target,text=m.params[0],m.params[1]
        if text.strip()=="!hello":
            dest=sender if target.lower()==nick.lower() else target
            return [f"PRIVMSG {dest} :Hello, {sender}!"]
    return []

def iter_lines(sock):
    buf=b""
    while True:
        chunk=sock.recv(4096)
        if not chunk:return
        buf+=chunk
        while b"\n" in buf:
            raw,buf=buf.split(b"\n",1); yield raw.rstrip(b"\r").decode("utf-8",errors="replace")

def connect(config):
    raw=socket.create_connection((config.host,config.port),timeout=30)
    return raw if not config.use_tls else ssl.create_default_context().wrap_socket(raw,server_hostname=config.host)

def run_session(config):
    with connect(config) as sock:
        if config.use_sasl:sock.sendall(encode_line("CAP LS 302"))
        sock.sendall(encode_line(f"NICK {config.nick}")); sock.sendall(encode_line(f"USER {config.nick} 0 * :IRC Handbook Bot"))
        for line in iter_lines(sock):
            print(f"<< {line}")
            for response in response_for_line(line,config.nick,config.channel,config.sasl_user,config.sasl_password):
                print(f">> {response}"); sock.sendall(encode_line(response))

def main():
    c=Config.from_env()
    if (c.sasl_user is None)!=(c.sasl_password is None): raise SystemExit("set both IRC_SASL_USER and IRC_SASL_PASSWORD")
    delay=2
    while True:
        try: run_session(c); delay=2
        except (OSError,ssl.SSLError) as e: print(f"connection error: {e}")
        print(f"reconnecting in {delay}s"); time.sleep(delay); delay=min(delay*2,60)
if __name__=="__main__":main()
