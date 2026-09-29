# Nick-kollisjon og server ERROR

Numeric `433` betyr at ønsket nick allerede er i bruk.

Undervisningsboten demonstrerer en deterministisk fallback:

```text
handbookbot -> handbookbot_
```

En større klient bør ha en bedre nick-policy, men poenget er at kollisjonen er en eksplisitt state transition.

Serverkommandoen `ERROR` behandles annerledes. Den avslutter den aktuelle sesjonen og løftes som en `ServerError` slik at reconnect-laget kan bestemme hva som skjer videre.

Dermed blandes ikke protokollfeil og reconnect-policy sammen.
