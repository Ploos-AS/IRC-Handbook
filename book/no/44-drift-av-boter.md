# Drift av IRC-boter

En bot som skal være tilgjengelig over tid er en tjeneste, ikke bare et terminalprogram du tilfeldigvis startet.

## Klassisk shellmodell

```text
SSH -> shell -> screen/tmux -> bot
```

Denne modellen er pedagogisk nyttig og finnes fortsatt i eksisterende miljøer.

## Tjenestemodell

På en server du administrerer selv kan en bot i stedet kjøres som en kontrollert systemtjeneste:

```text
service manager
      |
      +-- botprosess
             |
             +-- IRC
```

Det gir et naturlig sted for restart-policy, brukeridentitet og logging.

## Hva bør overvåkes?

Minst:

- kjører prosessen?
- er den koblet til forventet IRC-nettverk?
- reconnecter den etter nettverksbrudd?
- vokser logger eller database ukontrollert?
- feiler eksterne integrasjoner?
- er credentials fortsatt gyldige?

## Reconnect

En robust bot må tåle at:

- DNS feiler midlertidig
- TCP-forbindelsen brytes
- IRC-serveren restartes
- boten blir frakoblet
- serveren selv starter på nytt

Reconnect bør bruke kontrollert retry/backoff fremfor en aggressiv tett løkke.

## Logging og personvern

Logg det du trenger for drift, men ikke automatisk alt som blir sagt i alle kanaler.

Meldingsinnhold kan være persondata eller privat kommunikasjon. Logging, retention og backup må derfor være bevisste valg.
