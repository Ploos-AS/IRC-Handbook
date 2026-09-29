#!/usr/bin/env python3
"""Minimal educational IRC bot using only the Python standard library."""

from __future__ import annotations

import os
import socket
import ssl
import time
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    host: str
    port: int
    nick: str
    channel: str
    use_tls: bool = True

    @classmethod
    def from_env(cls) -> "Config":
        return cls(
            host=os.environ.get("IRC_HOST", "irc.example.net"),
            port=int(os.environ.get("IRC_PORT", "6697")),
            nick=os.environ.get("IRC_NICK", "handbookbot"),
            channel=os.environ.get("IRC_CHANNEL", "#handbook-test"),
            use_tls=os.environ.get("IRC_TLS", "1") != "0",
        )


def encode_line(line: str) -> bytes:
    if "\r" in line or "\n" in line:
        raise ValueError("IRC lines must not contain CR or LF")
    return (line + "\r\n").encode("utf-8")


def parse_privmsg(line: str):
    """Return (sender, target, message), or None for non-PRIVMSG lines."""
    if not line.startswith(":"):
        return None
    prefix, sep, rest = line[1:].partition(" ")
    if not sep:
        return None
    command, sep, rest = rest.partition(" ")
    if command.upper() != "PRIVMSG" or not sep:
        return None
    target, sep, message = rest.partition(" :")
    if not sep:
        return None
    sender = prefix.split("!", 1)[0]
    return sender, target, message


def response_for_line(line: str, nick: str, channel: str) -> list[str]:
    if line.startswith("PING "):
        return ["PONG " + line[5:]]

    parts = line.split()
    # Numeric 001 means registration succeeded.
    if len(parts) >= 2 and parts[1] == "001":
        return [f"JOIN {channel}"]

    msg = parse_privmsg(line)
    if not msg:
        return []

    sender, target, text = msg
    if text.strip() != "!hello":
        return []

    reply_target = sender if target.lower() == nick.lower() else target
    return [f"PRIVMSG {reply_target} :Hello, {sender}!"]


def iter_lines(sock):
    """Yield complete IRC lines while preserving partial TCP frames."""
    buf = b""
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            return
        buf += chunk
        while b"\n" in buf:
            raw, buf = buf.split(b"\n", 1)
            yield raw.rstrip(b"\r").decode("utf-8", errors="replace")


def connect(config: Config):
    raw = socket.create_connection((config.host, config.port), timeout=30)
    if not config.use_tls:
        return raw
    context = ssl.create_default_context()
    return context.wrap_socket(raw, server_hostname=config.host)


def run_session(config: Config) -> None:
    with connect(config) as sock:
        sock.sendall(encode_line(f"NICK {config.nick}"))
        sock.sendall(encode_line(f"USER {config.nick} 0 * :IRC Handbook Bot"))

        for line in iter_lines(sock):
            print(f"<< {line}")
            for response in response_for_line(line, config.nick, config.channel):
                print(f">> {response}")
                sock.sendall(encode_line(response))


def main() -> None:
    config = Config.from_env()
    delay = 2
    while True:
        try:
            run_session(config)
            delay = 2
        except (OSError, ssl.SSLError) as exc:
            print(f"connection error: {exc}")
        print(f"reconnecting in {delay}s")
        time.sleep(delay)
        delay = min(delay * 2, 60)


if __name__ == "__main__":
    main()
