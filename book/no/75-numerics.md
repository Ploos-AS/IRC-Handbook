# Numerics

Servere svarer ofte med tresifrede numeriske kommandoer.

Vi har allerede brukt flere:

```text
001  velkomst / registrering fullført
005  ISUPPORT
433  nickname in use
903  SASL success
904–907  SASL-relaterte feil
```

Parseren behandler ikke numerics som en egen wire-formatvariant. Kommando-feltet er ganske enkelt for eksempel `"005"`.

Eksempelboten har nå helperen `is_numeric()`, slik at høyere lag enkelt kan skille numeriske replies fra navngitte kommandoer som `PRIVMSG` og `PING`.

Betydningen av et numeric må tolkes i riktig protokollkontekst; nummeret alene er ikke hele state machine-en.
