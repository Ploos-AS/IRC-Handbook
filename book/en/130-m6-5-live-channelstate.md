# M6.5: live ChannelState

The channel model is now connected to the actual session loop. 005 configures protocol rules, 353 builds membership, 366 bounds the NAMES snapshot, and subsequent MODE and membership events update the same model.

The fake-server integration path also replays ISUPPORT, NAMES and MODE through runtime.

Further work remains for explicit snapshot generations, multiple channels and advanced resynchronization, but the major gap of not knowing who was already present when joining a channel is now closed.
