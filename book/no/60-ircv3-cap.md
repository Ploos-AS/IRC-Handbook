# IRCv3 CAP

IRCv3-funksjoner forhandles gjennom CAP i stedet for at klienten bare antar at serveren støtter dem.

Når SASL er konfigurert starter eksempelboten med:

```text
CAP LS 302
NICK handbookbot
USER handbookbot 0 * :IRC Handbook Bot
```

Serveren annonserer capabilities. Hvis `sasl` finnes, ber boten om den:

```text
CAP REQ :sasl
```

Etter `ACK` starter autentiseringen.

Dette gjør capability discovery til en eksplisitt del av state machine-en.
