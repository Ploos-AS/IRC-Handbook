# Dancer

Dancer hører hjemme i den historiske delen av IRC-botøkosystemet og er nyttig for å forstå eksisterende shell- og kanalbotmiljøer.

## Hvorfor dekke Dancer?

Boka handler ikke bare om å installere dagens mest moderne programvare. En IRC-operatør kan møte eldre botfamilier i:

- eksisterende shell-kontoer
- gamle kanaloppsett
- arkiverte konfigurasjoner
- migreringsprosjekter
- dokumentasjon fra tidligere IRC-miljøer

Dancer gir derfor enda et konkret eksempel på hvordan botfunksjonalitet historisk ble pakket og driftet.

## Samme analysemodell

Når du møter en Dancer-installasjon, kartlegg:

```text
prosess
  |
Unix-bruker
  |
konfigurasjon + state
  |
IRC-identitet
  |
kanaler/rettigheter
```

Finn også ut hvordan den konkrete versjonen håndterer nettverk, autentisering, reconnect, logging og eventuelle scripts eller utvidelser.

## Historie er ikke hardening

Gamle installasjonsguider kan være verdifulle historiske kilder, men sikkerhetsantakelser eldes.

Før en eksisterende Dancer-instans brukes videre på et moderne system må faktisk vedlikeholdsstatus, avhengigheter, nettverksstøtte og sikkerhetsfunksjoner vurderes.

Hvis kravene ikke kan oppfylles, er migrering et bedre svar enn å skjule begrensningen.
