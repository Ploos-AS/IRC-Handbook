# Irssi

Irssi is a classic terminal IRC client closely associated with Unix shell culture.

A traditional setup looks like:

```text
local terminal -> SSH -> shell server -> screen/tmux -> Irssi -> IRC network
```

You reconnect to the shell and attach to the existing terminal session, continuing where you left off.

We cover both Irssi and WeeChat because the architecture is not tied to one client. Their interfaces, configuration models and ecosystems differ, while the underlying IRC concepts remain the same.

Later we configure Irssi with TLS and SASL, run it under tmux or screen, test reconnection, and compare this persistent-client model with a dedicated bouncer.
