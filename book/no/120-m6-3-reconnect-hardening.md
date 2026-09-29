# M6.3: reconnect-hardening

Reconnect er en state machine, ikke bare en `while True`.

M6.3 gir oss:

- eksplisitt EOF/disconnect
- eksplisitt lokal shutdown
- health først ved numeric 001
- backoff-reset bare etter healthy session
- permanent auth-policyfeil adskilt fra reconnectbare feil

Sammen med M6.1 og M6.2 begynner eksempelklienten nå å ha tydelige sikkerhets- og lifecycle-grenser.

Neste hardening-steg bør samle serverfeatures fra 005 inn i den levende sesjonen, slik at CASEMAPPING, PREFIX og CHANMODES ikke bare finnes som parserfunksjoner, men faktisk styrer runtime-state.
