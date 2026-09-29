# Stateful CAP-forhandling

CAP-forhandling skjer over flere IRC-meldinger og må derfor behandles som tilstand, ikke som en enkelt if-setning.

Eksempelklienten har nå `Negotiation`, som eier en `CapabilityState` for hele forbindelsen.

Ved oppkobling sendes alltid:

```text
CAP LS 302
NICK ...
USER ...
```

Dermed kan også en klient uten SASL forhandle moderne IRCv3-funksjoner.
