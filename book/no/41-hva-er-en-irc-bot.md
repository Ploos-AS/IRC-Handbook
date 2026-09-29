# Hva er en IRC-bot?

En IRC-bot er i utgangspunktet en IRC-klient som styres av programlogikk i stedet for et menneske.

```text
vanlig klient: menneske -> IRC-klient -> IRC-server
bot:           program  -> IRC-klient -> IRC-server
```

På wire-nivå bruker begge IRC-protokollen.

## Hva kan en bot gjøre?

Avhengig av nettverket og kanalens regler kan en bot blant annet:

- svare på kommandoer
- hjelpe med kanaladministrasjon
- publisere varsler
- utføre automatiserte oppgaver
- integrere IRC med andre systemer
- føre begrenset driftslogg

En bot skal ikke gis mer tilgang enn oppgaven krever.

## Bot er ikke det samme som services

NickServ og ChanServ er typisk del av nettverkets serviceinfrastruktur. En vanlig bot kobler seg normalt til nettverket gjennom den vanlige klientprotokollen.

```text
IRC-nettverk
  +-- servere/services
  |
  +-- vanlige klienter
  |
  +-- boter
```

Dette skillet forklarer hvorfor en kanalbot ikke automatisk har privilegiene til nettverkets services.

## Bot er heller ikke bouncer

En bouncer bevarer og mellomlagrer brukerens IRC-sesjon. En bot er en egen automatisert IRC-deltaker.

De kan kjøre på samme server, men bør behandles som separate komponenter.
