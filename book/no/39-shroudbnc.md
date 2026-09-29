# ShroudBNC

ShroudBNC tilhører bouncer-familien som mange IRC- og shellbrukere vil møte i eldre eller eksisterende miljøer.

Den er relevant i håndboka fordi målet ikke bare er å lære ett nytt produkt, men å forstå IRC-infrastruktur godt nok til å orientere seg i forskjellige bouncer-oppsett.

## Les konfigurasjonen som arkitektur

Når du møter en ukjent bouncer, identifiser først:

- hvilken adresse og port klientene bruker
- hvordan klientene autentiseres
- hvilke upstream-nettverk som finnes
- hvordan upstream-identitet håndteres
- om TLS brukes downstream og upstream
- om meldinger lagres
- hvor konfigurasjon og state ligger
- hvilken Unix-bruker prosessen kjører som

Da kan du tegne:

```text
klient
  |
downstream
  |
bouncer
  |
upstream
  |
IRC-nettverk
```

Denne modellen fungerer uavhengig av produktnavn.

## Vedlikeholdsstatus betyr noe

Før eksisterende bouncer-programvare eksponeres på en moderne server må du kontrollere prosjektets faktiske vedlikeholdsstatus, sikkerhetsoppdateringer, avhengigheter og protokollstøtte.

Historisk eller eksisterende bruk er ikke i seg selv dokumentasjon på at en bestemt versjon er egnet for ny produksjonsdrift.
