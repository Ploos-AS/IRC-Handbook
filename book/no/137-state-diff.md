# Diff mellom snapshots

Når et transcript spilles videre er det nyttig å spørre hva som faktisk endret seg.

`snapshot_diff(before, after)` rapporterer kanalnøkler som er:

- lagt til
- fjernet
- endret

En enkel diff er ofte bedre pedagogisk enn å dumpe hele state etter hvert event. Den viser konsekvensen av protokollmeldingen.
