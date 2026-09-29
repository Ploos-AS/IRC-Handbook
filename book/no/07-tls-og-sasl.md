# TLS og SASL

To teknologier bør være standard i et moderne IRC-oppsett når nettverket støtter dem:

- **TLS** beskytter forbindelsen mellom klienten og IRC-serveren.
- **SASL** lar klienten autentisere en konto under oppkoblingen.

De løser forskjellige problemer og brukes gjerne sammen.

## TLS

Uten transportkryptering kan IRC-trafikk i prinsippet leses av systemer som kan observere den aktuelle nettverksforbindelsen. TLS krypterer transporten mellom klient og server og lar klienten kontrollere serverens sertifikat.

Klienten bør validere sertifikatet. Ikke slå av sertifikatkontroll bare for å få en feilmelding til å forsvinne.

## SASL

SASL står for Simple Authentication and Security Layer. I IRC brukes SASL til å autentisere klienten mot en konto som del av tilkoblingsprosessen.

Konseptuelt blir oppkoblingen:

```text
klient
  |
  +-- TLS-forbindelse
  |
  +-- SASL-autentisering
  |
  +-- registrert IRC-sesjon
```

Nøyaktige mekanismer og innstillinger avhenger av nettverket og klienten.

## Ikke legg passord i boka eller Git

Eksempler i denne boka bruker plassholdere:

```text
ACCOUNT_NAME
IRC_PASSWORD
```

Ikke commit ekte passord, SASL-hemmeligheter, API-nøkler eller private sertifikatnøkler til et repository.

Når vi senere automatiserer klienter, bouncere og boter, bruker vi egnede secret-mekanismer eller filer med begrensede rettigheter.

## TLS er ikke ende-til-ende-kryptering

TLS beskytter forbindelsen mellom klienten og serveren. IRC-serveren må fortsatt behandle meldingene for å levere dem videre. TLS alene gjør derfor ikke en vanlig IRC-kanal ende-til-ende-kryptert.

Dette skillet blir viktig i sikkerhets- og personvernkapitlene senere.
