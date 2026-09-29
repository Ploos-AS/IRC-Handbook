# Separating CAP and SASL

CAP negotiation and SASL data exchange are related but are not the same layer.

`Negotiation` decides which capabilities to request and when SASL begins. The ordinary message handler then processes `AUTHENTICATE +` and SASL result numerics.

Capability state therefore lives in one place while mechanism exchange remains separate.
