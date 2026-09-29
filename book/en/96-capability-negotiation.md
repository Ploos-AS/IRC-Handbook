# IRCv3 capability negotiation

IRCv3 extends IRC through negotiated capabilities rather than replacing the base protocol. A client commonly begins with `CAP LS 302`, learns what the server offers, requests features it understands, and receives ACK or NAK responses.

This opt-in model allows old and modern clients to coexist on the same IRC network.
