# NAMES as a channel snapshot

When a client joins a channel, users are usually already present. JOIN events alone therefore cannot construct complete membership state.

Numeric 353, RPL_NAMREPLY, supplies channel members and bootstraps `ChannelState`. Numeric 366 marks the end of the NAMES sequence, after which normal event replay keeps the model current.
