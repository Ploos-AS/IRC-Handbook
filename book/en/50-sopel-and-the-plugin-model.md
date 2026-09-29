# Sopel and the plugin model

Sopel demonstrates a different bot architecture: a general bot core combined with plugins.

```text
Sopel core
   |
   +-- IRC connection
   +-- configuration
   +-- dispatch
   |
   +-- plugins
```

A plugin can add a feature without reimplementing an IRC client.

Plugins still process network input, so validate arguments, avoid constructing shell commands from untrusted text, use timeouts for external services, limit filesystem and network access, avoid unnecessary logging and keep secrets out of source code.

Dependencies and external APIs are part of the security model. Document what a plugin needs and why.

Small, focused plugins are easier to test and reason about. We carry that principle into our own IRC bot later.
