# WeeChat

WeeChat is a terminal-based chat client well suited to persistent IRC setups on Unix and Linux systems.

It works well over SSH, needs no graphical desktop, can run inside tmux or screen, and fits naturally on a shell server or small VPS.

Our progression will be:

```text
terminal -> WeeChat -> IRC network
```

then:

```text
laptop -> SSH -> tmux -> WeeChat -> IRC network
```

and eventually:

```text
WeeChat -> soju/ZNC -> IRC network
```

Later labs configure TLS, SASL, autoconnect, buffers, logging and safe secret handling. The goal is to understand and maintain the configuration rather than merely copy a finished file.
