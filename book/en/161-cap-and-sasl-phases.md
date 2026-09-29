# CAP and SASL phases

At startup the bot sends `CAP LS 302`, `NICK`, and `USER`. CAP negotiation may then enter a SASL phase when authentication is configured and the server offers the required capability.

The phases are more than code organization. They define which protocol messages are meaningful. A SASL success or failure is a registration transition only while SASL is actually active. A stray or delayed 903 must therefore not move a connection from the CAP phase into registering.

When SASL is required, an authentication failure becomes fatal only when the client is actually in the SASL phase. After successful SASL, CAP negotiation is ended and registration continues.

This makes the state machine robust against messages that are syntactically valid but arrive in the wrong protocol context.