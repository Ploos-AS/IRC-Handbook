# Graceful shutdown

A long-running IRC client should terminate cleanly.

The minimal bot now handles SIGINT and SIGTERM through a small stop flag. When the active session gets an opportunity to shut down, it sends `QUIT :Shutting down` before closing the socket.

This is particularly useful under systemd or a container runtime, where termination normally begins with a signal. Shutdown state remains separate from the deterministic protocol parser.
