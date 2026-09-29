# Deterministic transcript replay

`replay_transcript()` accepts raw IRC lines, parses them and feeds them through ServerFeatures and ChannelRegistry in order.

The model becomes a simple pipeline: IRC transcript, parser, state engine, snapshot. Identical input should produce identical final state, turning real protocol sequences into useful regression tests.
