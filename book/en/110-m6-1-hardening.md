# M6.1: hardening the protocol client

Before the example bot approaches production use, its security boundaries need to be explicit.

M6.1 establishes four of them: authentication payloads are redacted from logs, SASL PLAIN is refused without TLS, AUTHENTICATE follows the 400-character chunking rule, and IRCv3 tag escapes are decoded in one pass.

These are hardening changes rather than new user features. Responsive socket shutdown and broader integration coverage still remain for later work.
