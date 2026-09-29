# Nick collision and server ERROR

Numeric 433 indicates that the requested nickname is already in use. The educational client demonstrates a deterministic fallback from `handbookbot` to `handbookbot_`.

A larger client needs a richer nickname policy, but the important lesson is that collision handling is an explicit state transition.

The server `ERROR` command instead terminates the current session and becomes a `ServerError`, leaving reconnect policy to the outer layer.
