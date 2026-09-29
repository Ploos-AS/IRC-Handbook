# IRCv3 message tags

IRCv3 message tags appear at the beginning of a line after `@` and can carry metadata without changing the underlying command.

The parser supports tags with and without values and decodes the basic escape forms. The `!hello` command therefore continues to work when a server prefixes PRIVMSG with IRCv3 tags.

This demonstrates why protocol parsing deserves its own layer.
