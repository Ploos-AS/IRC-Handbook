# Multiline CAP in practice

When CAP LS is split across messages, the client must wait until the continuation marker disappears before choosing capabilities.

The `Negotiation` state therefore returns no request for intermediate LS fragments. This prevents premature negotiation from overlooking capabilities advertised later in the sequence.
