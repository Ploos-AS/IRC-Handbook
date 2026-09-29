# One owner per protocol transition

A protocol implementation quickly becomes fragile when several parts of the program can react to the same control message. Before M6.13, registration behavior could exist both in the general message handler and in CAP negotiation. The same event could then potentially cause duplicate responses or duplicate state transitions.

M6.13 therefore follows the rule **one owner per protocol transition**. `Registration` owns registration-related events: CAP, SASL, nickname collision, and welcome. The ordinary message path no longer needs a parallel stateless implementation of those transitions.

This rule also makes tests more precise. A 433 test should exercise Registration because Registration knows the current nickname and registration phase. A SASL-result test must first establish the required CAP/SASL sequence. Otherwise the test constructs a state that a real client should not normally occupy.

The pattern generalizes beyond IRC: when one component owns protocol state, invariants, logging, replay, and error handling become much easier to reason about.