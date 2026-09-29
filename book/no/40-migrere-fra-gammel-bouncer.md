# Migrere fra en gammel bouncer

Migrering bør behandles som flytting av state og identitet, ikke bare som installasjon av et nytt program.

## Kartlegg først

Dokumenter den gamle løsningen:

```text
brukere
nettverk
servere
porter
TLS
nick
IRC-kontoer
autojoin-kanaler
historikk/buffere
scripts/moduler
DNS
servicebruker
backup
```

Ikke kopier secrets inn i migreringsnotater som skal i Git.

## Bygg parallelt

En trygg modell er å sette opp den nye bounceren separat:

```text
gammel BNC ----> IRC

ny ZNC/soju ---> testnettverk/testkonto
```

Test klienttilkobling, TLS, SASL, reconnect og historikk før du flytter den virkelige bruken.

## Flytt funksjon, ikke nødvendigvis filformat

Gamle og nye bouncere har forskjellige konfigurasjonsmodeller.

I stedet for å prøve å oversette hver linje mekanisk, oversett intensjonen:

```text
"denne brukeren skal koble til nettverk X"
"denne kontoen skal bruke SASL"
"disse kanalene skal være tilgjengelige"
"historikk skal beholdes i N dager"
```

Konfigurer så dette på den nye plattformens måte.

## Cutover

Når den nye løsningen er verifisert:

1. ta siste backup av gammel konfigurasjon/state
2. planlegg et kort byttevindu
3. flytt klientene til ny endpoint
4. verifiser identitet og kanaler
5. overvåk feil
6. behold gammel løsning avslått, men tilgjengelig for rollback en begrenset periode
7. fjern gamle credentials og eksponerte tjenester når migreringen er godkjent

Dette er samme disiplin vi senere bruker når vi migrerer hele IRC-hostingmiljøer.
