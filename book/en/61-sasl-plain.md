# SASL PLAIN

SASL PLAIN uses a base64-encoded authentication field. Base64 is **not encryption**, so real SASL PLAIN authentication belongs inside a TLS-protected connection.

The example negotiates SASL, sends `AUTHENTICATE PLAIN`, waits for `AUTHENTICATE +`, sends the encoded account/password payload, waits for numeric 903 and then sends `CAP END`.

Real credentials come from `IRC_SASL_USER` and `IRC_SASL_PASSWORD`, never from Git.
