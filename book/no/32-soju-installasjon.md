# soju: moderne IRC-bouncer

soju er en IRC-bouncer utviklet med moderne IRC- og IRCv3-bruk som en sentral del av modellen.

## Arkitektur

```text
IRC-klient(er)
      |
      v
     soju
      |
      +---- IRC-nettverk A
      +---- IRC-nettverk B
      +---- IRC-nettverk C
```

Bounceren blir et vedvarende mellomlag mellom klientene og nettverkene.

## Separat tjeneste

Som med ZNC bør soju kjøre som en uprivilegert tjenesteidentitet, ikke som root.

På en produksjonsserver ønsker vi et tydelig skille:

```text
root/system
   |
   +-- administrasjon

soju service
   |
   +-- bouncerprosess
   +-- konfigurasjon
   +-- state/database
```

## Installer etter plattformens dokumentasjon

Pakkenavn, versjoner, databasevalg og serviceintegrasjon kan variere mellom distribusjoner og soju-versjoner. Kontroller derfor dokumentasjonen for den versjonen du faktisk installerer.

Etter installasjon tester vi først lokalt eller i et kontrollert nett før en lytter eksponeres mot Internett.

## Data er en del av tjenesten

Når bounceren lagrer kontoer, nettverkskonfigurasjon og historikk, er ikke lenger bare konfigurasjonsfilen viktig. State/databasen må inngå i backup-, tilgangs- og oppgraderingsplanen.
