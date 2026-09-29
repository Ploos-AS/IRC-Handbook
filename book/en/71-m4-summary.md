# M4 summary: from bot user to protocol client

M4 began with established bot ecosystems and ended with our own small IRC client.

The reader has now encountered classic and modern bots, plugins, TCP framing, structured IRC parsing, core commands, IRCv3 CAP, SASL PLAIN, authentication policy, nickname collisions, server ERROR, a local fake server, success and failure integration tests, graceful shutdown and deterministic reconnect backoff.

The example remains deliberately small so the complete path from socket to bot command can be understood.

M5 changes focus from building a bot to studying IRC itself in depth: grammar, numerics, modes, ISUPPORT, CTCP, capability negotiation and modern IRCv3 semantics.
