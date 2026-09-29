# Kontoer og IRC-services

På IRC er **nick** og **konto** to forskjellige ting. Dette er et av de viktigste konseptene å lære før vi setter opp permanente IRC-forbindelser.

## Nick er ikke konto

Et nick er navnet du bruker i en aktiv IRC-forbindelse:

```text
/nick Ada
```

En konto er en identitet som et IRC-nettverk kan autentisere. På nettverk som tilbyr kontoer kan du derfor være logget inn på kontoen `ada` selv om ditt aktive nick er noe annet.

Denne forskjellen blir viktig når vi senere bruker flere klienter og bouncere.

## Services

Mange tradisjonelle IRC-nettverk tilbyr funksjoner gjennom såkalte **services**. De kan se ut som IRC-brukere, men er tjenester levert av nettverket.

Vanlige navn er:

- NickServ — kontoer og nick-relaterte funksjoner
- ChanServ — kanalregistrering og kanaladministrasjon
- MemoServ — meldings-/memo-funksjoner på enkelte nettverk

Eksakte kommandoer varierer mellom nettverk. Bruk derfor nettverkets egen dokumentasjon i stedet for å anta at alle services fungerer likt.

## Identifisering

Historisk har mange klienter og brukere identifisert seg ved å sende en kommando til NickServ etter tilkobling. Det fungerer fortsatt på enkelte nettverk, men moderne klienter bør normalt bruke **SASL** når nettverket støtter det.

Fordelen er at autentiseringen skjer som del av oppkoblingen, før vanlig IRC-bruk begynner.

## Kontoen følger ikke automatisk mellom nettverk

En konto på ett IRC-nettverk er normalt ikke en global IRC-konto. Har du konto `ada` på nettverk A, betyr det ikke at du eier eller kan bruke samme konto på nettverk B.

Tenk derfor på kontoen som:

```text
IRC-nettverk + kontonavn
```

ikke som én universell IRC-identitet.
