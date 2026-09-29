# NAMES-generasjoner

En NAMES-liste er et snapshot, ikke bare en strøm av medlemmer som skal legges til for alltid.

`ChannelState` markerer derfor en aktiv NAMES-generasjon når første 353 kommer. Alle nick som observeres i snapshotet registreres i `names_seen`.

Ved 366 fjernes medlemmer som fantes i gammel state, men som ikke ble observert i den nye generasjonen. Dermed kan NAMES også brukes til resynkronisering.
