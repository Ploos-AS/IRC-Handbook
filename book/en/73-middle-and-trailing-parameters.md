# Middle and trailing parameters

IRC distinguishes space-free middle parameters from a final trailing parameter that may contain spaces.

`COMMAND one two :three four` becomes `["one", "two", "three four"]`. The colon marks trailing-parameter syntax and is not part of the value.

This is why `PRIVMSG #retro :Hello everyone` can carry a message containing spaces.
