# Migrating from an old bouncer

Treat migration as movement of state and identity rather than merely installing another program.

First inventory users, networks, servers, ports, TLS, nicks, IRC accounts, auto-joined channels, history, scripts/modules, DNS, service identity and backups. Keep secrets out of Git-based migration notes.

Build the replacement separately and test client connectivity, TLS, SASL, reconnect behaviour and history before moving real use.

Translate **intent**, not necessarily configuration syntax. A requirement such as “this account authenticates to network X with SASL” should be implemented using the new bouncer's own model rather than mechanically translating old files.

At cutover, take a final backup, move clients to the new endpoint, verify identity and channels, monitor failures, retain a powered-down rollback path for a limited period, then revoke old credentials and remove obsolete exposed services after the migration is accepted.
