# CASEMAPPING

IRC identifiers cannot always be compared correctly with an ordinary lowercase operation.

Servers may advertise `ascii`, `rfc1459` or `strict-rfc1459` CASEMAPPING. RFC1459 mappings make additional ASCII characters equivalent; traditional rfc1459 also treats ^ and ~ as equivalent while strict-rfc1459 does not.

The minimal client now provides `irc_casefold()` and `irc_equal()`. Direct-message target detection therefore uses IRC identifier semantics rather than ordinary string comparison.
