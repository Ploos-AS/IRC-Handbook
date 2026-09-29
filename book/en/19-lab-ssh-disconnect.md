# Lab: survive an SSH disconnect

Connect to the shell:

```sh
ssh user@shell.example.net
```

Create a tmux session:

```sh
tmux new -s irc-lab
```

Start `weechat`, connect to an IRC network and join an appropriate test channel.

Detach using `Ctrl-b`, then `d`, and verify the session with:

```sh
tmux ls
```

Exit SSH. Reconnect later and run:

```sh
tmux attach -t irc-lab
```

WeeChat should still be running.

Repeat the exercise with an unplanned local SSH/network interruption, then reconnect and attach again.

The lab demonstrates the distinction between the local SSH transport and the remote process plus IRC connection. That distinction is the core of the classic IRC shell model.
