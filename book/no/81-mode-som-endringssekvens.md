# MODE som endringssekvens

En MODE-melding er ikke bare en streng med flagg. Den beskriver en sekvens av endringer.

```text
MODE #retro +ov-v alice bob carol
```

kan leses som:

```text
+o alice
+v bob
-v carol
```

Pluss og minus endrer retning for mode-tegnene som følger. Parametrene konsumeres i den rekkefølgen serverens mode-regler krever.

Minimal-klienten representerer hver operasjon som en `ModeChange` med retning, mode og eventuelt parameter.
