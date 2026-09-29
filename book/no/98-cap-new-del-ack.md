# CAP NEW, DEL og ACK

Capability-state kan endres etter registrering.

`CAP NEW` annonserer nye capabilities. `CAP DEL` fjerner capabilities som ikke lenger er tilgjengelige. `CAP ACK` bekrefter endringer klienten har bedt om.

Minimal-klienten skiller derfor mellom:

- `available`: det serveren tilbyr
- `enabled`: capabilities som er aktivert

Når en capability slettes, fjernes den også fra enabled-state.
