# WeeChat

WeeChat er en terminalbasert chat-klient og passer svært godt til et permanent IRC-oppsett på en Unix/Linux-maskin.

## Hvorfor terminal?

En terminalklient har noen praktiske egenskaper:

- fungerer godt over SSH
- krever lite grafisk miljø
- kan kjøres inne i tmux eller screen
- passer godt på en shell-server eller liten VPS
- kan styres effektivt med tastaturet

## Første start

På et system der WeeChat allerede er installert:

```sh
weechat
```

WeeChat har sin egen kommando- og konfigurasjonsmodell. Ikke kopier credentials blindt fra tilfeldige eksempler på nettet; vi bygger en sikker konfigurasjon senere.

## Arkitekturen vi skal bygge

Først:

```text
terminal -> WeeChat -> IRC-nettverk
```

Deretter:

```text
laptop -> SSH -> tmux -> WeeChat -> IRC-nettverk
```

Og senere kan WeeChat være en klient foran en bouncer:

```text
WeeChat -> soju/ZNC -> IRC-nettverk
```

Dette er et godt eksempel på IRCs lagdelte natur.

## Konfigurasjon som ferdighet

Målet med kapitlene senere i boka er ikke bare å gi en ferdig konfigurasjonsfil. Du skal forstå serverdefinisjoner, TLS, SASL, autoconnect, buffers, logging og hvordan hemmeligheter håndteres.

Da kan du vedlikeholde oppsettet selv når klienten eller nettverket endrer seg.
