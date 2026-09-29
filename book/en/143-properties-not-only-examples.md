# Properties, not only examples

An example test asks whether one exact result is correct. A property states a rule that should hold across many sequences.

Registry invariants should survive every parseable mutation; QUIT should remove a nick from all channels; identical transcripts should yield identical snapshots; and a completed NAMES resync should not retain stale members.

These rules test architecture rather than one hand-written protocol sequence.
