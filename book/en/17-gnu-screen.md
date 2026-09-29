# GNU Screen: the classic solution

GNU Screen was a common way to keep terminal IRC clients running on shell servers long before tmux became widespread, making it an important part of IRC shell culture.

Start a session with:

```sh
screen -S irc
```

Run `irssi` or `weechat`. With the default bindings, detach using `Ctrl-a` followed by `d`.

List and resume sessions with:

```sh
screen -ls
screen -r irc
```

Both Screen and tmux solve the same basic problem: the SSH connection may disappear while the terminal multiplexer and IRC client continue running. New examples in this book primarily use tmux, while Screen remains covered for classic and existing shell environments.
