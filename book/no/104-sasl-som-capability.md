# SASL som capability

SASL er nå del av samme capability-maskin som resten av IRCv3-forhandlingen.

Hvis legitimasjon finnes og serveren annonserer `sasl`, tas den med i CAP REQ. Når serveren ACK-er SASL, starter klienten:

```text
AUTHENTICATE PLAIN
```

Hvis SASL er markert som obligatorisk, er manglende annonsering eller eksplisitt avvisning en autentiseringsfeil.

Dermed er «SASL ønsket» og «SASL påkrevd» fortsatt to forskjellige policyer.
