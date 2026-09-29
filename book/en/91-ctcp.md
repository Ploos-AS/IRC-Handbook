# CTCP: a protocol layer inside IRC

CTCP, the Client-To-Client Protocol, uses the text carried by IRC PRIVMSG and NOTICE to transport small structured messages.

A CTCP frame is delimited by the 0x01 character, as in VERSION, ACTION or PING frames. It is not a new outer IRC command: the server still sees PRIVMSG or NOTICE.

The minimal client now has `parse_ctcp()` and `ctcp_frame()` so CTCP is kept separate from ordinary chat text.
