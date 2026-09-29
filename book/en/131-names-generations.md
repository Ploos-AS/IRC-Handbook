# NAMES generations

A NAMES list is a snapshot rather than a stream of members that should only ever be appended.

`ChannelState` starts an active NAMES generation on the first 353 and records every observed nick. At 366, members left over from old state but absent from the new generation are removed, allowing NAMES to act as a resynchronization mechanism.
