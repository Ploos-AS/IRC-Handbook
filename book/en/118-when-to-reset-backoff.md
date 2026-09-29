# When to reset backoff

Exponential backoff protects both client and server from rapid reconnect loops.

A connection that opens and immediately closes must not reset the backoff counter. Otherwise a server that accepts TCP and drops it before IRC registration can create a reconnect storm.

Backoff is therefore reset only after a session reached healthy state.
