# Persistence, history and multi-client use

Three bouncer properties are often confused.

**Persistent upstream connection** means the bouncer remains connected to IRC when your client disconnects.

**History or playback** means messages may be retained and presented when a client returns. This is implementation-dependent and introduces privacy and data-retention considerations.

**Multi-client operation** means several devices can use the same bouncer environment concurrently. That requires more state coordination than merely preserving one upstream connection, and modern IRCv3 features can improve the model considerably.

For troubleshooting, think in layers:

```text
IRC client
    |
client <-> bouncer
    |
bouncer state/history
    |
bouncer <-> upstream
    |
IRC network
```

Identifying which layer owns a problem becomes one of the most useful skills in the rest of the book.
