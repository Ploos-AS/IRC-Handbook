# CTCP framing and validation

CTCP is old and small, which makes direct string construction tempting. We still keep framing in a dedicated function.

`ctcp_frame()` rejects CR, LF and the CTCP delimiter in commands and arguments, while the outer IRC line encoder performs its own CR/LF validation.

The layers remain explicit: CTCP data → CTCP frame → PRIVMSG/NOTICE → IRC line → TCP. Each layer can validate its own boundary.

Next we return to modern IRCv3 capabilities and message tags.
