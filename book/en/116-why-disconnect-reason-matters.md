# Why disconnect reason matters

An IRC session can end for very different reasons: local shutdown, clean EOF, server ERROR, transport failure or authentication policy.

Treating all of them as a normal return discards information needed by reconnect policy. The example now uses an explicit `ConnectionClosed` for EOF and `SessionResult` for controlled local termination.
