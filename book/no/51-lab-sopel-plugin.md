# Lab: en liten Sopel-plugin

Målet er å demonstrere plugin-arkitekturen uten å bygge en komplisert bot.

## Funksjon

Vi ønsker en enkel kommando:

```text
!hello
```

som svarer med en kort, statisk melding.

Dette krever:

- ingen shell-kommando
- ingen database
- ingen ekstern API
- ingen operatorstatus
- ingen hemmelighet

Det er et godt første plugin-eksempel.

## Struktur

Den konseptuelle flyten er:

```text
IRC PRIVMSG
    |
Sopel parser/dispatch
    |
hello-plugin
    |
svar via Sopel
    |
IRC PRIVMSG
```

Bruk plugin-API-et og syntaksen som gjelder for den Sopel-versjonen du faktisk har installert.

## Test

Test minst:

1. boten starter med pluginen aktiv
2. `!hello` gir forventet svar
3. vanlig kanaltekst ignoreres
4. ukjente kommandoer krasjer ikke pluginen
5. reconnect påvirker ikke pluginens evne til å svare etter at forbindelsen er tilbake

## Ingen ekstra privilegier

Botens oppgave er bare å svare.

Den trenger derfor ikke kanaloperatorstatus.

Dette er minste privilegium i praksis: rettighetene bestemmes av funksjonen, ikke av at programmet kalles en «bot».
