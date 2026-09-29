# Live CASEMAPPING

IRC identifiers cannot always be compared with ordinary lowercase rules. With ASCII casemapping, square and curly brackets remain distinct; RFC1459 casemapping may treat them as equivalent.

Runtime now uses `ServerFeatures.casemapping` when deciding whether PRIVMSG or CTCP targets the bot directly. An unknown advertised mapping falls back to rfc1459 in this educational example rather than crashing the session.
