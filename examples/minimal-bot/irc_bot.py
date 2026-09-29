#!/usr/bin/env python3
"""Minimal educational IRC bot using only the Python standard library."""

from __future__ import annotations
import base64, os, socket, ssl, time
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    host: str
    port: int
    nick: str
    channel: str
    use_tls: bool = True
    sasl_user: str | None = None
    sasl_password: str | None = None

    @classmethod
    def from_env(cls) -> "Config":
        return cls(
            host=os.environ.get("IRC_HOST", "irc.example.net"),
            port=int(os.environ.get("IRC_PORT", "6697")),
            nick=os.environ.get("IRC_NICK", "handbookbot"),
            channel=os.environ.get("IRC_CHANNEL", "#handbook-test"),
            use_tls=os.environ.get("IRC_TLS", "1") != "0",
            sasl_user=os.environ.get("IRC_SASL_USER"),
            sasl_password=os.environ.get("IRC_SASL_PASSWORD"),
        )

    @property
    def use_sasl(self) -> bool:
        return self.sasl_user is not None and self.sasl_password is not None

def encode_line(line: str) -> bytes:
    if "\r" in line or "\n" in line:
        raise ValueError("IRC lines must not contain CR or LF")
    return (line + "\r\n").encode()

def parse_privmsg(line: str):
    if not line.startswith(":"): return None
    prefix, sep, rest = line[1:].partition(" ")
    if not sep: return None
    command, sep, rest = rest.partition(" ")
    if command.upper() != "PRIVMSG" or not sep: return None
    target, sep, message = rest.partition(" :")
    if not sep: return None
    return prefix.split("!", 1)[0], target, message

def sasl_plain(user: str, password: str) -> str:
    raw = ("\0" + user + "\0" + password).encode()
    return base64.b64encode(raw).decode("ascii")

def response_for_line(line: str, nick: str, channel: str,
                      sasl_user: str | None = None,
                      sasl_password: str | None = None) -> list[str]:
    if line.startswith("PING "): return ["PONG " + line[5:]]
    parts = line.split()
    use_sasl = sasl_user is not None and sasl_password is not None

    if use_sasl and " CAP " in f" {line} ":
        if " LS " in f" {line} " and "sasl" in line.split(" :", 1)[-1].split():
            return ["CAP REQ :sasl"]
        if " ACK " in f" {line} " and "sasl" in line.split(" :", 1)[-1].split():
            return ["AUTHENTICATE PLAIN"]

    if use_sasl and line == "AUTHENTICATE +":
        return ["AUTHENTICATE " + sasl_plain(sasl_user, sasl_password)]

    if use_sasl and len(parts) >= 2 and parts[1] == "903":
        return ["CAP END"]

    if len(parts) >= 2 and parts[1] == "001":
        return [f"JOIN {channel}"]

    msg = parse_privmsg(line)
    if not msg: return []
    sender, target, text = msg
    if text.strip() != "!hello": return []
    reply_target = sender if target.lower() == nick.lower() else target
    return [f"PRIVMSG {reply_target} :Hello, {sender}!"]

def iter_lines(sock):
    buf = b""
    while True:
        chunk = sock.recv(4096)
        if not chunk: return
        buf += chunk
        while b"\n" in buf:
            raw, buf = buf.split(b"\n", 1)
            yield raw.rstrip(b"\r").decode("utf-8", errors="replace")

def connect(config: Config):
    raw = socket.create_connection((config.host, config.port), timeout=30)
    if not config.use_tls: return raw
    return ssl.create_default_context().wrap_socket(raw, server_hostname=config.host)

def run_session(config: Config) -> None:
    with connect(config) as sock:
        if config.use_sasl:
            sock.sendall(encode_line("CAP LS 302"))
        sock.sendall(encode_line(f"NICK {config.nick}"))
        sock.sendall(encode_line(f"USER {config.nick} 0 * :IRC Handbook Bot"))
        for line in iter_lines(sock):
            print(f"<< {line}")
            for response in response_for_line(
                line, config.nick, config.channel,
                config.sasl_user, config.sasl_password
            ):
                print(f">> {response}")
                sock.sendall(encode_line(response))

def main() -> None:
    config = Config.from_env()
    if (config.sasl_user is None) != (config.sasl_password is None):
        raise SystemExit("set both IRC_SASL_USER and IRC_SASL_PASSWORD")
    delay = 2
    while True:
        try:
            run_session(config); delay = 2
        except (OSError, ssl.SSLError) as exc:
            print(f"connection error: {exc}")
        print(f"reconnecting in {delay}s")
        time.sleep(delay); delay = min(delay * 2, 60)

if __name__ == "__main__":
    main()
