# MODE som faktisk state

Resultatet fra MODE-parseren brukes nå til å endre lokal kanaltilstand.

Medlemsmodes lagres per medlem. List modes som ban lagres som sett av verdier. Modes som key og limit har egne verdier, mens parameterløse modes lagres som enkle flagg.

Dermed kan:

```text
MODE #c +klib secret 25 *!*@bad
```

oppdatere key, limit, invite-only og banlisten i én hendelse.

Parsing avgjør *hva meldingen betyr*. State-laget avgjør *hvordan dagens modell endres*.
