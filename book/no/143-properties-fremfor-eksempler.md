# Properties fremfor bare eksempler

En eksempeltest spør om ett bestemt resultat er riktig. En property uttrykker en regel som skal holde for mange sekvenser.

Eksempler:

- registry-invariants skal holde etter enhver parsebar mutasjon
- QUIT skal fjerne nicket fra alle kanaler
- samme transcript skal gi samme snapshot
- et avsluttet NAMES-resync skal ikke beholde stale medlemmer

Disse reglene tester arkitekturen, ikke bare én håndskrevet protokollsekvens.
