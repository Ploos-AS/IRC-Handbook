# Vår egen minimale IRC-bot

Nå fjerner vi bot-frameworket og ser direkte på protokollen.

Koden ligger i:

```text
examples/minimal-bot/
```

## Registrering

Etter TLS-tilkoblingen sender første versjon:

```text
NICK handbookbot
USER handbookbot 0 * :IRC Handbook Bot
```

Serverens numeriske svar `001` forteller at registreringen er fullført. Først da sender boten:

```text
JOIN #handbook-test
```

Dette er en viktig detalj: IRC-klienten er en liten state machine, ikke bare en serie tilfeldige tekstlinjer.

## PING/PONG

Når serveren sender:

```text
PING :token
```

må boten svare:

```text
PONG :token
```

Eksemplet gjør dette direkte.

## PRIVMSG

En kanalmelding kan se slik ut:

```text
:alice!user@host PRIVMSG #handbook-test :!hello
```

Parseren trekker ut sender, target og melding. Bare eksakt `!hello` utløser svar.

## Ingen shell

Botkommandoen blir aldri satt inn i en shell-kommando. Det er et bevisst sikkerhetsvalg.

Første versjon skal være liten nok til at hele dataflyten kan forstås.
