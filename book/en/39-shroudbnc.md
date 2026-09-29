# ShroudBNC

ShroudBNC is part of the bouncer family that IRC and shell users may encounter in older or existing environments.

When approaching an unfamiliar bouncer, identify the client listener, downstream authentication, upstream networks and identities, TLS on both sides, history storage, configuration/state location and Unix service identity.

Reduce the deployment to:

```text
client -> downstream -> bouncer -> upstream -> IRC network
```

This model remains useful regardless of product name.

Before exposing existing bouncer software on a modern server, verify its actual maintenance status, security updates, dependencies and protocol support. Historical or existing use alone does not establish that a particular version is suitable for a new production deployment.
