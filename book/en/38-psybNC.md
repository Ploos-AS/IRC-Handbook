# psyBNC

psyBNC is a well-known name from the classic IRC bouncer and shell era.

The goal here is primarily to understand its architecture and recognize older installations, documentation and migration scenarios.

A typical arrangement was:

```text
local IRC client -> psyBNC -> IRC network
```

It could run on a shell account alongside terminal clients and bots.

Historical guides may contain assumptions about TLS, passwords, permissions, compilation and network exposure that do not belong in a modern deployment. Separate useful architectural knowledge from operational practices that must be reassessed.

The book therefore does not treat old configuration examples as a current security baseline.
