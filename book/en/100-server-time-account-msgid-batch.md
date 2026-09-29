# server-time, account, msgid and batch

server-time can provide the server's event timestamp rather than the time a local client happened to receive the message. Account-related tags can associate an event with an authenticated account, msgid can identify a message, and batch associates a message with an IRCv3 batch context.

Capability state describes what has been negotiated; message tags describe metadata on a particular event. The two layers are related but should not be confused.

Next we make session-level CAP negotiation stateful so desired IRCv3 features and SASL can be selected systematically.
