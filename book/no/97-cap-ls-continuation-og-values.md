# CAP LS continuation og capability values

En capability-liste kan være større enn én IRC-melding. Serveren kan derfor sende flere `CAP LS`-linjer og markere at flere følger med `*`.

Eksempelklientens `CapabilityState` samler slike deler før den publiserer den komplette listen.

Capabilities kan også ha verdier:

```text
sasl=PLAIN,EXTERNAL
```

Derfor lagres annonserte capabilities som navn pluss valgfri verdi, ikke bare som et sett med navn.
