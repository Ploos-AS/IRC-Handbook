# ChannelRegistry

One IRC connection may participate in multiple channels.

`ChannelRegistry` owns an independent `ChannelState` for each channel and uses the server's CASEMAPPING for channel keys. Channel-specific events are routed to the relevant state, while global NICK and QUIT events are replayed across every known channel.
