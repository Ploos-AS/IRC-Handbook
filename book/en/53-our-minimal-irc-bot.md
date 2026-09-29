# Our minimal IRC bot

We now remove the bot framework and work directly with the protocol.

The runnable example lives in `examples/minimal-bot/`.

After establishing TLS, the first version sends `NICK` and `USER`. It waits for numeric `001` before sending `JOIN`, making the client a small state machine rather than a random sequence of text writes.

It answers server `PING` with `PONG` and parses the subset of `PRIVMSG` needed for an exact `!hello` command.

No IRC argument is passed to a shell. The first version is deliberately small enough for the complete data flow to remain understandable.
