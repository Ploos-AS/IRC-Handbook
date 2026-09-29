# Akkumulere flere 005-linjer

ISUPPORT passer ikke nødvendigvis på én melding. En server kan spre tokens over flere 005-linjer.

`ServerFeatures.update()` merger nye tokens inn i eksisterende state.

Et token med minus, for eksempel:

```text
-PREFIX
```

fjerner den tidligere annonserte verdien. Klienten faller da tilbake til en konservativ standard der det finnes en definert fallback.
