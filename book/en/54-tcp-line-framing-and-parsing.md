# TCP, line framing and parsing

IRC is line-oriented, but TCP is a byte stream. One `recv()` call does not necessarily equal one IRC message.

A client must buffer bytes until a complete line is available. The example bot's `iter_lines()` implements this behaviour.

IRC lines are terminated by CRLF. `encode_line()` adds the terminator and rejects input that already contains CR or LF, preventing future user-controlled data from accidentally becoming additional IRC commands.

The minimal parser supports only what the bot currently needs. Later chapters extend the model with tags, prefixes, capabilities and additional command forms instead of pretending a simple split operation is a complete IRC parser.
