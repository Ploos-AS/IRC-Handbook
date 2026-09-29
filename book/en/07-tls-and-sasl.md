# TLS and SASL

Two technologies should be normal parts of a modern IRC setup when supported:

- **TLS** protects transport between the client and IRC server.
- **SASL** authenticates the client to an IRC account during connection setup.

They solve different problems and are commonly used together.

Clients should validate the server certificate rather than disabling verification to work around certificate errors.

Examples in this book use placeholders such as:

```text
ACCOUNT_NAME
IRC_PASSWORD
```

Never commit real passwords, SASL secrets, API keys or private certificate keys to a repository. Later automation examples will use appropriate secret handling or permission-restricted files.

TLS is transport encryption, not ordinary IRC end-to-end encryption. The IRC server still processes messages in order to route them. We return to this distinction in the security and privacy chapters.
