# ChannelState from ServerFeatures

`ChannelState.configure()` copies the relevant live protocol rules from `ServerFeatures`: CASEMAPPING, membership modes from PREFIX, and CHANMODES.

The membership index and MODE parser therefore follow the rules advertised by the server. State that is correct under RFC1459 casemapping is not necessarily correct under ASCII casemapping.
