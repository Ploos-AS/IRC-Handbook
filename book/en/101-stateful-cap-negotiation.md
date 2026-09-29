# Stateful CAP negotiation

CAP negotiation spans multiple IRC messages and therefore needs connection state rather than a single conditional.

The example client now has a `Negotiation` object owning a `CapabilityState` for the connection. Every connection sends CAP LS 302 before registration messages, allowing modern IRCv3 features to be negotiated even when SASL is not configured.
