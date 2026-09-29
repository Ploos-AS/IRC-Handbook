# Sopel og plugin-modellen

Sopel illustrerer en annen måte å bygge IRC-boter på: en generell botkjerne kombinert med plugins.

## Del ansvar

```text
Sopel core
   |
   +-- IRC connection
   +-- configuration
   +-- dispatch
   |
   +-- plugin A
   +-- plugin B
   +-- vår plugin
```

Dette gjør det mulig å legge til en funksjon uten å implementere hele IRC-klienten på nytt.

## Plugin er fortsatt kode som behandler nettverksinput

En plugin kan motta nick, kanaltekst, argumenter og andre data fra IRC.

Derfor gjelder de samme reglene:

- valider input
- ikke bygg shell-kommandoer av ukontrollert tekst
- bruk timeouts mot eksterne tjenester
- begrens fil- og nettverkstilgang
- ikke logg mer enn nødvendig
- hold secrets utenfor kildekoden

## Avhengigheter

Plugins kan trekke inn biblioteker og eksterne API-er. Det gjør dependency management til en del av botens sikkerhetsmodell.

Dokumenter hva pluginen trenger og hvorfor.

## Små plugins

En god plugin gjør én tydelig ting. Store integrasjoner bør deles opp slik at feil, permissions og testing blir lettere å forstå.

Dette prinsippet tar vi med videre når vi senere skriver vår egen IRC-bot.
