# Snapshot pluss event-replay

En praktisk kanalmodell består av to faser:

```text
353 NAMES snapshot
        ↓
366 end of NAMES
        ↓
JOIN / PART / KICK / QUIT
NICK / MODE
        ↓
oppdatert ChannelState
```

Snapshotet gir starttilstanden. Hendelsene holder den fersk.

Samme modell gjør også testing enklere: et lagret IRC-transcript kan spilles gjennom parseren og ende i deterministisk state.
