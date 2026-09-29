# Registration as a state machine

An IRC client is not fully ready when the TCP connection is established. Before normal operation it must pass through a protocol sequence: CAP negotiation, NICK and USER, optional SASL authentication, and finally welcome numeric 001.

The minimal bot models this sequence explicitly with `Registration`. The object has a phase describing where the connection is in registration. Ordinary message handlers therefore do not have to guess whether a 903, 904, or CAP ACK belongs to an active registration.

This illustrates an important systems principle: protocol state should be explicit data. When state exists only implicitly in control flow, reconnects, delayed messages, and unexpected ordering become much harder to reason about and test.

M6.13 also separates registration from `SessionState`. Registration describes how we become registered. SessionState describes what the server has told us about the current connection. ChannelRegistry describes observed channel state. These concepts should remain separate.