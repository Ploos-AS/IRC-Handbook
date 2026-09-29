# M6.7: an observable state engine

The state engine now has three properties that make it easier to trust and teach: deterministic snapshots, explicit diffs and invariants during transcript replay.

This opens the door to a corpus of realistic transcripts, fuzzing parser-to-state transitions and property-style rules such as a QUIT never leaving the same nick in a channel.

The educational bot does not need to become a complete IRC library. The goal is to expose how a robust protocol client can be constructed layer by layer.
