# SASL as a capability

SASL is now part of the same capability state machine as other IRCv3 features. If credentials are configured and the server advertises sasl, it is included in CAP REQ. An ACK for SASL starts AUTHENTICATE PLAIN.

When SASL is required, absence or rejection is an authentication-policy failure. Optional SASL and mandatory SASL remain distinct policies.
