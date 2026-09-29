# Deterministisk fuzzing

Tilfeldige tester er mest nyttige når en feil kan reproduseres.

`mutate_transcript()` bruker derfor en eksplisitt seed. Den lager varianter av et kjent transcript ved blant annet å endre case, duplisere meldinger og gjøre små syntaktiske variasjoner.

Samme seed og samme corpus gir samme mutationssekvens. En CI-feil kan dermed kjøres igjen lokalt.
