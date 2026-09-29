# The problem with blocking recv

An IRC connection may remain quiet for a long time. If the program blocks indefinitely in `recv()`, a signal handler that merely sets a stop flag is insufficient because the main loop may never regain control.

The example client now uses a short socket timeout as a polling boundary. A timeout means no data yet, not a broken connection.
