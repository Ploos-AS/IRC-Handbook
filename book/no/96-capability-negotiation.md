# IRCv3 capability negotiation

IRCv3 utvider IRC gjennom capabilities i stedet for å erstatte grunnprotokollen.

Klienten starter typisk med:

```text
CAP LS 302
```

Serveren annonserer hvilke utvidelser som er tilgjengelige. Klienten velger dem den forstår og ønsker, og serveren kan ACK eller NAK forespørselen.

Dette gjør moderne funksjoner opt-in og lar eldre og nyere klienter eksistere på samme nettverk.
