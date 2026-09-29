# SASL PLAIN requires TLS

PLAIN does not protect the password at the transport layer. The example configuration therefore refuses SASL credentials when TLS is disabled.

The policy is simple: SASL PLAIN with TLS is allowed; SASL PLAIN without TLS stops before connecting. Test harnesses should exercise lower protocol layers without weakening the production-facing configuration policy.
