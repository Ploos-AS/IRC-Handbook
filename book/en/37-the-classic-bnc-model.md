# The classic BNC model

Before modern multi-client bouncers, the basic idea was simple:

```text
IRC client -> BNC -> IRC network
```

The BNC commonly ran on a shell server with stable connectivity, allowing the local client to disconnect without necessarily losing the upstream IRC connection.

A classic shell environment might combine screen, Irssi, a BNC and Eggdrop under one account.

This solved persistent connectivity and made the IRC session independent of an unreliable local connection. A simple relay, however, did not automatically provide structured history, synchronized multi-client state, modern IRCv3 integration or today's TLS and credential practices.

Understanding this model explains why modern bouncers evolved as they did.
