# One CAP state machine

Protocol state should have one authoritative owner.

Previously both `Negotiation` and `actions_for_message()` could interpret CAP messages, creating two implementations of the same state machine. CAP is now handled only by `Negotiation`.
