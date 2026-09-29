# 153. NAMES som snapshot

En NAMES-liste er ikke live state. Den er et snapshot som leveres over én eller flere `353`-meldinger og avsluttes med `366`.

Det blir viktig når vanlige IRC-hendelser kommer mens snapshotet overføres. En bruker kan for eksempel stå i en gammel `353`, sende `PART`, og deretter dukke opp igjen i en senere del av snapshotet.

Eksempelboten bygger derfor NAMES i en separat pending state. Live-hendelser journalføres mens NAMES pågår. Ved `366` installeres snapshotet atomisk, og journalen replayes i samme rekkefølge som hendelsene ble mottatt.

Dermed kan eldre snapshot-data ikke vinne over nyere live-data.
