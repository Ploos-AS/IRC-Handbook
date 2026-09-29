# Lab: WeeChat og Irssi via ZNC

Målet er å bevise at den lokale IRC-klienten nå kan forsvinne mens ZNC beholder upstream-sesjonen.

## Før testen

Du skal ha:

- en fungerende ZNC-instans
- TLS på klientforbindelsen når den går over et ubeskyttet nett
- en ZNC-bruker
- minst ett konfigurert IRC-nettverk
- upstream TLS
- SASL der nettverket og kontoen støtter det

## Koble klienten til ZNC

Konfigurer WeeChat eller Irssi med ZNC som server i stedet for å koble direkte til IRC-nettverket.

Bruk verdiene fra din egen ZNC-konfigurasjon:

```text
server: BOUNCER_HOST
port:   BOUNCER_TLS_PORT
user:   ZNC_LOGIN
secret: ZNC_SECRET
TLS:    enabled + certificate validation
```

Eksakt syntaks varierer mellom klient- og ZNC-versjoner.

## Test 1: vanlig IRC

Kontroller at du kan:

- koble til
- se forventet nick/konto
- gå inn i en kanal
- sende og motta meldinger

## Test 2: avslutt klienten

Avslutt WeeChat eller Irssi helt.

Vent en stund mens ZNC fortsetter å kjøre.

Start klienten igjen og koble til ZNC.

Kontroller at upstream-forbindelsen ikke måtte bygges fra bunnen av bare fordi den lokale klienten var borte.

## Test 3: playback

Send eller motta testmeldinger mens den lokale klienten er frakoblet, med samtykke fra deltakerne i testen.

Koble til igjen og undersøk hvordan ZNC presenterer buffered historikk.

## Test 4: bytt klient

Koble fra WeeChat og prøv Irssi mot den samme ZNC-kontoen.

Dette demonstrerer hovedpoenget:

```text
IRC-identiteten og upstream-sesjonen
er ikke lenger bundet til ett lokalt klientprogram.
```

I neste del gjentar vi ideen med soju og undersøker hvordan en mer IRCv3-orientert multiclient-modell skiller seg fra ZNC-opplevelsen.
