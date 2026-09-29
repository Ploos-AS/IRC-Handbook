# Deterministic fuzzing

Randomized tests are most useful when failures can be reproduced.

`mutate_transcript()` therefore accepts an explicit seed and creates variations of a known transcript by changing case, duplicating messages and making small syntactic mutations.

The same seed and corpus produce the same mutation sequence, so a CI failure can be replayed locally.
