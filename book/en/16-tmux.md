# tmux: keep the terminal session alive

`tmux` is a terminal multiplexer. It allows a program on the shell server to continue running after your SSH connection ends.

Start a named session:

```sh
tmux new -s irc
```

Then run, for example, `weechat`. With the default bindings, detach using the `Ctrl-b` prefix followed by `d`.

Later:

```sh
ssh user@shell.example.net
tmux attach -t irc
```

Use `tmux ls` to list sessions.

The key distinction is that tmux is not an IRC bouncer. It preserves the terminal program; the IRC client itself remains connected to the IRC network.
