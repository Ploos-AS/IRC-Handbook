# 157. Our own channel lifecycle

There is a difference between another user leaving a channel and the client itself leaving it.

When another user sends PART or is kicked, that user is removed from the member list. When our own client parts or is kicked, there is no longer an active local channel session. The complete channel model should therefore be removed.

Likewise, our own JOIN establishes a channel session. This makes the registry describe channels the client is actually participating in rather than channels it happened to visit in the past.
