# psyBNC

psyBNC er et kjent navn fra den klassiske IRC-bouncer- og shell-epoken.

Målet her er først og fremst å forstå arkitekturen og kunne kjenne igjen eldre installasjoner og dokumentasjon.

## Typisk rolle

```text
lokal IRC-klient
       |
       v
    psyBNC
       |
       v
IRC-nettverk
```

På en shell-konto kunne dette kjøre side om side med terminalklienter og boter.

## Hvorfor er det fortsatt relevant å lære om?

Du kan møte psyBNC i:

- gamle shell-guider
- historiske konfigurasjoner
- arkiverte IRC-miljøer
- migreringsprosjekter
- diskusjoner om klassisk IRC-infrastruktur

Det gir også perspektiv på hvorfor dagens bouncere har funksjonene de har.

## Ikke kopier gammel sikkerhetspraksis

En gammel guide kan inneholde antakelser om TLS, passord, filrettigheter, kompilering og nettverkseksponering som ikke passer et moderne system.

Når vi analyserer en historisk konfigurasjon skiller vi derfor mellom:

```text
arkitektur som fortsatt er nyttig å forstå
              og
driftspraksis som må vurderes på nytt
```

Boka bruker ikke gamle konfigurasjonseksempler som sikkerhetsfasit.
