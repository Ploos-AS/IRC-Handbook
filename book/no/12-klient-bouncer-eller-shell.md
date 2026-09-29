# Klient, bouncer eller shell?

Før vi bygger videre er det nyttig å skille mellom tre arkitekturer.

## Lokal klient

```text
PC -> IRC-klient -> IRC-nettverk
```

Enkelt og tilstrekkelig for mange brukere.

## Fjernkjørt klient på shell

```text
PC -> SSH -> tmux -> IRC-klient -> IRC-nettverk
```

IRC-klienten kjører kontinuerlig på en annen maskin. Du fjernstyrer selve klienten.

## Lokal klient via bouncer

```text
PC -> IRC-klient -> bouncer -> IRC-nettverk
```

Her kjører brukergrensesnittet lokalt. Bounceren vedlikeholder forbindelsen og presenterer IRC videre til klienten.

## Flere enheter

Bouncer-modellen blir spesielt interessant når flere klienter skal brukes:

```text
Desktop ---+
           |
Laptop ----+--> bouncer --> IRC-nettverk
           |
Telefon ---+
```

Moderne bouncere kan tilby langt mer enn bare en permanent TCP-forbindelse, blant annet historikk og funksjoner for flere klienter.

Ingen av modellene er universelt riktig. Gjennom boka bygger vi dem praktisk slik at du kan velge arkitektur ut fra egne behov.
