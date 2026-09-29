# Controlled QUIT

When local shutdown is requested, the client makes a best-effort attempt to send `QUIT :Shutting down` before the socket closes.

If the transport is already gone, failure to send QUIT must not prevent process termination. Graceful shutdown means attempting a protocol-level close, not waiting forever for proof that the server received it.
