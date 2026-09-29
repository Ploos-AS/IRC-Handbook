# PREFIX and CHANMODES from the server

PREFIX describes membership status modes and their visible prefix characters. CHANMODES groups channel modes according to their parameter rules.

`ServerFeatures` exposes both in parsed form, providing one authoritative runtime source for the rules needed by MODE parsing and channel state.

The next connection is to make live ChannelState consume those values directly.
