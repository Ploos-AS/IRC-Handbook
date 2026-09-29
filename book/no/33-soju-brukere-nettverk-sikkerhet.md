# soju: brukere, nettverk og sikkerhet

Det er nyttig å skille tre identitetsnivåer:

```text
person
  |
  +-- soju-bruker
         |
         +-- IRC-nettverk A -> IRC-konto A
         +-- IRC-nettverk B -> IRC-konto B
```

soju-brukeren autentiserer klienten mot bounceren. Hvert upstream-nettverk kan ha sin egen IRC-konto og SASL-konfigurasjon.

## Downstream

Klientforbindelsen til en Internett-eksponert bouncer bør beskyttes med TLS og korrekt sertifikatvalidering.

## Upstream

Forbindelsen fra soju til IRC-nettverket bør bruke TLS når nettverket tilbyr det. Bruk SASL for kontoautentisering der det støttes og passer.

Dermed får vi:

```text
klient
  |
 TLS + bouncer-login
  |
 soju
  |
 TLS + IRC SASL
  |
IRC-nettverk
```

## Secrets

Hold passord og andre autentiseringshemmeligheter utenfor Git. Beskytt konfigurasjon og database med passende Unix-rettigheter og inkluder hemmelighetshåndtering i backup-planen.

## Flere nettverk

En viktig gevinst ved bouncerlaget er at klienten kan få tilgang til flere IRC-nettverk gjennom én vedvarende tjeneste. Nettverkene er fortsatt separate IRC-verdener med egne kontoer, kanaler og regler.
