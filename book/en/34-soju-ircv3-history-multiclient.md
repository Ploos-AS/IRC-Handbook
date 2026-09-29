# soju: IRCv3, history and multi-client use

soju is particularly interesting for IRC use across several devices:

```text
Desktop ---+
Laptop ----+--> soju --> IRC network
Phone -----+
```

This requires more than reconnecting a single client. The bouncer represents persistent IRC state to multiple downstream connections.

IRCv3 capabilities are negotiated; clients, servers and bouncers do not necessarily support the same feature set. Later protocol chapters examine CAP negotiation on the wire.

History can provide context after disconnection, but it also creates stored user data. Operators must consider retention, access, backups, deletion and disk usage.

The modern mental model is:

```text
devices <-> bouncer state <-> IRC networks
```

rather than one terminal client permanently running inside screen.
