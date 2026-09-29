# M6.6: a small IRC state engine

The example has moved from one channel with a member list to a small replayable state engine: ServerFeatures feeds a ChannelRegistry, each channel owns a ChannelState, and each state combines NAMES generations with live events.

This provides deterministic multi-channel state, NAMES-based resynchronization and global handling of nick changes and quits.

Complete IRC clients have further edge cases, but the model is now large enough to teach the architecture without hiding the major state problems behind a library.
