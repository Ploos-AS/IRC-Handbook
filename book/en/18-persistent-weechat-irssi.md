# Persistent WeeChat or Irssi

We can now combine the pieces:

```sh
ssh user@shell.example.net
tmux new -s irc
weechat
```

Detach from tmux after the client is connected. Later reconnect over SSH and use:

```sh
tmux attach -t irc
```

The same architecture works with Irssi.

Be precise about what persistence means: tmux lets the IRC client **process continue without the local SSH terminal**. A server reboot, client crash or network failure can still interrupt IRC.

A useful setup therefore combines a persistent terminal session, client reconnect/autoconnect behaviour and correct TLS/SASL configuration. Later, dedicated services and bouncers provide another operational model.
