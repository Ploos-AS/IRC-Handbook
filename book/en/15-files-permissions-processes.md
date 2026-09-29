# Files, permissions and processes

Three Unix concepts are essential for using a shell account safely: the home directory, file permissions and processes.

After login, commands such as:

```sh
pwd
ls -la
```

help inspect the current environment.

`ls -l` displays Unix permission information. A private file may, for example, be restricted with:

```sh
chmod 600 private-file
```

Do not use `chmod 777` as a universal fix for permission problems.

When you launch `weechat`, it runs as a process owned by your account. You can inspect processes with commands such as `ps` and `ps -u "$USER"`.

Programs attached directly to a terminal may be affected when the SSH connection disappears. Terminal multiplexers such as **tmux** and **screen** solve this problem:

```text
SSH connection -> tmux -> WeeChat -> IRC network
```

The SSH connection can disappear while the tmux session and WeeChat continue running on the server.
