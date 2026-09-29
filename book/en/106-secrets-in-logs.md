# Secrets do not belong in logs

SASL PLAIN sends a base64-encoded authentication payload. Base64 is encoding, not encryption, so the payload must be treated as a secret.

The example bot still sends the real AUTHENTICATE line to the server but logs only `AUTHENTICATE <redacted>`. Observability should show that an authentication step happened without copying credentials into terminals, CI output or log aggregation systems.
