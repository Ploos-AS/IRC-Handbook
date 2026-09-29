# Lab: soju med flere klienter

Målet er å demonstrere forskjellen mellom en permanent forbindelse og et miljø som faktisk brukes fra flere klienter.

## Forutsetninger

Du trenger:

- en fungerende soju-instans
- en testbruker
- TLS på eksponert downstream-forbindelse
- minst ett upstream IRC-nettverk
- upstream TLS
- SASL der nettverket støtter det
- to IRC-klientinstanser

## Klient A

Koble den første klienten til soju og verifiser:

- innlogging mot bounceren
- upstream-forbindelse
- forventet nick/konto
- kanaler
- sending og mottak

## Klient B

Koble deretter en annen klientinstans mot samme soju-bruker.

Det kan for eksempel være:

```text
A = WeeChat på laptop
B = en annen klientinstans på desktop
```

Poenget er ikke klientmerket, men at begge går gjennom samme bouncerlag.

## Frakobling

Koble fra klient A mens B fortsetter.

Send testtrafikk i et kontrollert testmiljø. Koble A inn igjen og undersøk hvordan klienten og bounceren presenterer historikk og state.

Gjenta motsatt vei.

## Legg til nettverk nummer to

Konfigurer et annet IRC-nettverk og observer at:

```text
soju-bruker
   |
   +-- nettverk A
   +-- nettverk B
```

ikke betyr at kontoene på de to IRC-nettverkene er den samme identiteten.

## Resultat

Labben skal gjøre denne modellen konkret:

```text
flere klienter
      |
      v
vedvarende bouncer-state
      |
      v
flere uavhengige IRC-nettverk
```
