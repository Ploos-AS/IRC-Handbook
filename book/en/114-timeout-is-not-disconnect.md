# A timeout is not a disconnect

A socket timeout means that no data arrived during a short interval. EOF means the peer closed the stream, while a socket error means the transport failed.

Only the latter two indicate that the connection is no longer usable. Keeping these cases distinct prevents a quiet IRC channel from causing pointless reconnect loops.
