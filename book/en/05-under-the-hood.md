# A first look under the hood

IRC is unusually approachable as a networking protocol because much of its communication can be understood as lines of text.

A server may send:

```text
PING :example
```

and the client replies:

```text
PONG :example
```

When you type a message in `#retro`, the client conceptually sends:

```text
PRIVMSG #retro :Hello everyone!
```

And the client command:

```text
/join #retro
```

normally results in a protocol command such as:

```text
JOIN #retro
```

The leading slash therefore belongs to the client's command interface, not normally to the IRC protocol itself.

This distinction becomes useful when writing bots, debugging connections, understanding bouncers, learning IRCv3 and operating servers. Later we will build a minimal IRC client that connects to a test server, answers `PING`, joins a channel and sends a message.
