# soju: IRCv3, historikk og multiclient

soju er spesielt interessant når IRC brukes fra flere enheter.

## Flere klienter

```text
Desktop ---+
Laptop ----+--> soju --> IRC-nettverk
Mobil -----+
```

Dette er mer enn bare reconnect. Bounceren må representere en vedvarende IRC-tilstand overfor flere klientforbindelser.

## IRCv3

IRCv3 består av utvidelser til IRC-protokollen som klienter, servere og bouncere kan forhandle om.

Ikke alle nettverk og klienter støtter de samme funksjonene. Derfor skal en moderne IRC-stack kunne oppdage og forhandle capabilities i stedet for å anta at alt finnes overalt.

Senere i protokolldelen går vi ned på wire-nivå og ser på CAP-forhandlingen.

## Historikk

Historikk gjør det mulig for en klient å få kontekst etter å ha vært frakoblet. Moderne protokollstøtte kan gjøre dette mer strukturert enn klassisk tekst-playback.

Men historikk betyr også lagrede brukerdata.

Operatøren må derfor ta stilling til:

- hvor mye som lagres
- hvor lenge det lagres
- hvem som kan lese dataene
- backup
- sletting
- diskbruk

Bekvemmelighet og dataminimering må balanseres bevisst.

## Bounceren som synkroniseringspunkt

Den moderne modellen kan oppsummeres som:

```text
enheter <-> bouncer-state <-> IRC-nettverk
```

Det er en annen mental modell enn den klassiske løsningen der én terminalklient bare står permanent i screen.
