# A local fake IRC server

Unit tests can exercise the parser without a socket. We now test the transport layer as well.

The repository contains a small fake IRC server in `examples/minimal-bot/test_integration.py`. It listens only on loopback and exists solely as a test peer.

The scripted session covers NICK/USER registration, numeric 001, JOIN, PING/PONG and a `!hello` PRIVMSG response.

The integration test deliberately uses plaintext TCP only on `127.0.0.1` with an ephemeral local port. This is not a recommendation for plaintext IRC over the Internet; production connections remain TLS-enabled by default.
