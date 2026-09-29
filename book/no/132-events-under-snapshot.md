# Events mens snapshotet bygges

IRC er asynkront. En JOIN kan komme mens flere 353-linjer fortsatt er på vei.

Hvis snapshot-slutten blindt sletter alt som ikke sto i 353, kan et helt ferskt JOIN forsvinne.

Når en JOIN mottas under aktiv NAMES-generasjon legges nicket derfor både til medlemsstate og til generasjonens observerte sett.

Snapshot og live events må samarbeide, ikke konkurrere.
