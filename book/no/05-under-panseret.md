# Første titt under panseret

IRC er spesielt godt egnet til å lære nettverksprotokoller fordi mye av kommunikasjonen kan forstås som tekstlinjer.

Du trenger ikke forstå dette kapitlet fullt ut ennå. Målet er å vise hva som finnes under klientens brukergrensesnitt.

## PING og PONG

En server må kunne oppdage forbindelser som ikke lenger fungerer. Du vil derfor møte meldinger av typen:

```text
PING :example
```

Klienten svarer:

```text
PONG :example
```

Vanlige IRC-klienter gjør dette automatisk.

## En kanalmelding

Når du skriver:

```text
Hei alle sammen!
```

i `#retro`, vil klienten i prinsippet sende en IRC-melding tilsvarende:

```text
PRIVMSG #retro :Hei alle sammen!
```

Navnet `PRIVMSG` kan virke forvirrende: kommandoen brukes både for meldinger til enkeltbrukere og til kanaler.

## JOIN

Når du skriver:

```text
/join #retro
```

vil klienten normalt sende en protokollkommando som:

```text
JOIN #retro
```

Skråstreken er altså vanligvis del av klientens kommandogrensesnitt, ikke selve IRC-protokollen.

## Hvorfor dette er nyttig

Denne forskjellen blir svært viktig når vi senere:

- skriver vår egen IRC-bot
- feilsøker forbindelser
- analyserer IRC-logger
- arbeider med bouncere
- lærer IRCv3
- undersøker serverfunksjoner

Etter hvert skal vi bygge en minimal IRC-klient som kan koble seg til en testserver, svare på `PING`, gå inn i en kanal og sende en melding.
