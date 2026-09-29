# Regresjonssperre for message tags

Tag-unescaping hadde tidligere blitt implementert som en kjede av `replace()`-operasjoner. Det er fristende kode, men kan dekode tekst som ble produsert av en tidligere erstatning.

Testene dekker nå eksplisitt:

- kjent escape
- ukjent escape
- backslash som produserer en sekvens som ikke skal dekodes på nytt
- avsluttende backslash

Single-pass-oppførselen er dermed en testet kontrakt.
