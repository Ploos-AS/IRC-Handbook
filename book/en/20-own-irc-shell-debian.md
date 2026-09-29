# Your own IRC shell on Debian

A small VPS lets you build your own IRC shell without being an administrator on a shared shell service. Debian is the reference system used in this book.

The initial architecture is deliberately simple:

```text
Laptop -> SSH -> Debian VPS -> tmux -> WeeChat/Irssi
```

A basic client environment may include:

```sh
sudo apt update
sudo apt install tmux weechat irssi
```

Package availability and versions vary between Debian releases, so verify the release you actually operate.

Do not run the IRC client as root. Use an ordinary Unix account and add bouncers and bots later as separate components after the basic shell path is stable and understood.
