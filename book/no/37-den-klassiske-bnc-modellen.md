# Den klassiske BNC-modellen

Før moderne multiclient-bouncere var den grunnleggende ideen enkel:

```text
IRC-klient -> BNC -> IRC-nettverk
```

BNC-en kjørte ofte på en shell-server med stabil nettforbindelse. Brukeren kunne koble den lokale klienten fra uten nødvendigvis å miste den eksterne IRC-forbindelsen.

## Shell-kulturen

Et klassisk oppsett kunne se slik ut:

```text
shell-konto
  |
  +-- screen
  +-- Irssi
  +-- BNC
  +-- Eggdrop
```

Shell-kontoen var dermed både arbeidsmiljø og et lite personlig tjenestemiljø.

## Hva løste BNC-en?

Den klassiske modellen var særlig nyttig for:

- vedvarende IRC-forbindelse
- en stabil ekstern vert
- reconnect fra forskjellige lokale maskiner
- å flytte IRC-sesjonen bort fra en ustabil oppringt eller lokal forbindelse

Historisk kontekst er viktig: behovene oppstod i en verden med andre klienter, nettforbindelser og sikkerhetsforventninger enn i dag.

## Hva manglet den enkle modellen?

En enkel relay er ikke automatisk det samme som:

- strukturert meldingshistorikk
- synkronisert state mellom flere samtidige klienter
- moderne IRCv3-integrasjon
- moderne credential- og TLS-håndtering

Det er nettopp disse forskjellene som forklarer utviklingen mot dagens bouncere.
