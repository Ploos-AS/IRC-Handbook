# Forord

IRC er en av Internetts eldste fortsatt levende samtaleprotokoller. Den er enkel nok til at du kan forstå trafikken med egne øyne, men fleksibel nok til å støtte store nettverk, permanente identiteter, bouncere, boter og egne servere.

Denne boka er laget for deg som vil forstå IRC i praksis. Vi begynner med den første tilkoblingen og bygger gradvis opp mot et komplett, permanent IRC-miljø.

Du trenger ikke tidligere erfaring med Unix, shell-kontoer, boter eller serverdrift.

## Hva du skal lære

Etter boka skal du kunne:

- koble deg til et IRC-nettverk og bruke de viktigste kommandoene
- forstå kanaler, nicks, kontoer og modes
- bruke TLS og SASL
- bruke terminalklienter som Irssi og WeeChat
- forstå og bruke shell-kontoer
- holde IRC-miljøet ditt i gang via SSH, tmux eller screen
- sette opp og bruke en IRC-bouncer
- forstå forskjellen mellom ZNC, soju og eldre bouncer-tilnærminger
- kjøre og administrere IRC-boter
- skrive en enkel IRC-bot selv
- lese grunnleggende IRC-protokolltrafikk
- forstå moderne IRCv3-funksjoner
- drifte et lite IRC-miljø på VPS eller egen server
- gjøre fornuftige sikkerhets- og personvernvalg

## Bokas røde tråd

Vi starter enkelt:

```text
Din maskin -> IRC-klient -> IRC-nettverk
```

Mot slutten har vi bygget dette:

```text
Laptop ----+
Phone ------+--> Bouncer --> IRC-nettverk
Web --------+       |
                    +--> Bot
                    +--> Flere IRC-nettverk
                    |
                 Shell/VPS
                    |
             SSH + tmux + verktøy
```

Målet er ikke bare å lære kommandoer. Målet er å forstå hvordan hele IRC-økosystemet henger sammen.
