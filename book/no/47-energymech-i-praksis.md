# EnergyMech i praksis

EnergyMech representerer en annen gren av den klassiske IRC-botkulturen.

Målet med denne labben er å bruke samme driftsmetode som for Eggdrop og se hvor mye av kunnskapen som faktisk er produktuavhengig.

## Arkitektur

```text
shell/VPS
   |
egen botbruker
   |
EnergyMech
   |
IRC-nettverk
```

## Før installasjon

Kontroller den konkrete distribusjonens eller upstream-prosjektets vedlikeholdsstatus, build-instruksjoner og støttede sikkerhetsfunksjoner.

Historiske guider er nyttige for kultur og arkitektur, men skal ikke automatisk brukes som dagens hardening-guide.

## Kartlegg konfigurasjonen

Finn ut hvordan den konkrete versjonen representerer:

- botens nick og identitet
- IRC-server
- TLS dersom tilgjengelig
- kontoautentisering/SASL dersom tilgjengelig
- kanaler
- botbrukere og rettigheter
- logging
- reconnect

Hvis en ønsket sikkerhetsfunksjon ikke støttes av versjonen du vurderer, skal det dokumenteres som en begrensning i stedet for å late som funksjonen finnes.

## Samme driftskrav

Uansett botmotor vil vi ha:

- uprivilegert prosess
- minst mulig kanalrettighet
- secrets utenfor Git
- kontrollert reconnect
- begrenset logging
- backup av nødvendig state
- dokumentert oppgraderingsvei
