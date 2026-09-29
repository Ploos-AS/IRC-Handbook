# Fra plugin til egen bot

En plugin-ramme gir mye gratis:

- IRC-tilkobling
- parsing
- event-dispatch
- reconnect
- konfigurasjon
- logging
- ofte støtte for moderne protokollfunksjoner

Når vi skriver vår egen bot må vi selv ta ansvar for flere av disse lagene.

## To måter å bygge på

```text
A: plugin

funksjon
  |
Sopel
  |
IRC
```

mot:

```text
B: egen klient

funksjon
  |
egen parser/state
  |
TLS/socket
  |
IRC
```

Plugin-modellen er ofte riktig når målet er å lage IRC-funksjonalitet raskt og sikkert på toppen av et etablert rammeverk.

Egen klient er pedagogisk verdifull fordi den viser hvordan IRC faktisk fungerer.

## Neste steg

Vi skal nå skrive en minimal bot selv.

Første versjon trenger bare å kunne:

1. opprette en TLS-forbindelse
2. sende registreringskommandoer
3. lese IRC-linjer
4. svare korrekt på `PING`
5. gå inn i en kanal
6. lese `PRIVMSG`
7. svare på én eksplisitt kommando
8. reconnecte kontrollert

Ingen framework-magi.

Når dette virker vil både Eggdrop, EnergyMech, Dancer og Sopel være lettere å forstå, fordi vi kjenner mekanikken de bygger på.
