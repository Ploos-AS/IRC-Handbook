# IRCv3 CAP

IRCv3 features are negotiated through CAP rather than assumed by the client.

When SASL is configured, the example bot begins with `CAP LS 302` alongside normal NICK/USER registration. If the server advertises `sasl`, the client requests it with `CAP REQ :sasl`.

After ACK, authentication begins. Capability discovery is therefore an explicit part of the client state machine.
