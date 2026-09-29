# Snapshot plus event replay

A practical channel model has two phases. The 353 NAMES replies establish the initial snapshot, 366 closes that sequence, and JOIN, PART, KICK, QUIT, NICK and MODE events keep the same state current.

This also makes deterministic testing possible: an IRC transcript can be replayed through the parser and should produce a predictable final state.
