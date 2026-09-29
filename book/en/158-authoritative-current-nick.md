# 158. Authoritative current nick

The nick we request is not necessarily the nick the session ultimately uses.

During registration, nick collisions or other server behavior may affect identity. After successful registration, numeric `001` contains the nick by which the server actually knows the client.

M6.12 therefore treats the nick parameter in `001` as the authoritative current nick. Later NICK events update it further.

This matters when recognizing our own JOIN, PART and KICK events and when deciding whether a PRIVMSG is addressed directly to the client.
