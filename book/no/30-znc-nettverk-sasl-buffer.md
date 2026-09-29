# ZNC: nettverk, SASL og buffer

Etter at klienten kan koble sikkert til ZNC, legger vi til et upstream IRC-nettverk.

## To forbindelser

```text
WeeChat
   |
   | klientforbindelse
   v
  ZNC
   |
   | upstream-forbindelse
   v
IRC-nettverk
```

TLS bør vurderes på begge forbindelsene.

## Upstream SASL

Hvis IRC-nettverket støtter SASL, kan ZNC autentisere kontoen når den etablerer upstream-forbindelsen.

Dette er IRC-kontoen vi lærte om tidligere, ikke ZNC-brukerens innlogging.

Bruk plassholdere i dokumentasjon:

```text
IRC_ACCOUNT
IRC_SECRET
```

og oppbevar ekte hemmeligheter utenfor Git.

## Buffer og playback

En viktig ZNC-funksjon er å beholde meldinger for klienter som har vært frakoblet.

Dette gir en annen brukeropplevelse enn bare:

```text
tmux -> WeeChat
```

fordi klienten kan være helt avsluttet og senere hente informasjon via bounceren.

Bufferstørrelse og lagring er også en personvern- og driftsbeslutning. Mer historikk betyr mer data å beskytte.

## Moduler

ZNC har et modulsystem som kan utvide oppførselen.

Aktiver bare funksjoner du forstår og faktisk trenger. Hver ekstra komponent gir mer konfigurasjon, mer state og potensielt større angrepsflate.
