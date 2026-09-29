# M5: from lines to a protocol platform

During M5 the educational client has grown from basic line handling into explicit layers: TCP/TLS, IRC framing and parsing, numerics and ISUPPORT, CASEMAPPING/PREFIX/CHANMODES, MODE and ChannelState, CTCP, IRCv3 tags and CapabilityState, and finally stateful CAP/SASL negotiation.

The goal is not to compete with mature IRC libraries. It is to let the reader trace the mechanisms and understand why robust clients need them.

The example is not yet production-hardened. Secret handling, stricter SASL/TLS policy and additional protocol edge cases form a natural bridge into the next section.
