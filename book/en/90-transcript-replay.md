# Transcript replay

With deterministic parsing and state handling, a stored IRC transcript can be replayed to reconstruct a channel step by step.

This is useful for testing because membership logic does not require a connection to a public IRC network. It also enables larger fixture-based tests in which a known stream of protocol lines has an expected final state snapshot.

Next we turn to CTCP: a small secondary protocol carried inside PRIVMSG and NOTICE.
