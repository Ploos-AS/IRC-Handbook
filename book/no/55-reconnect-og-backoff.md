# Reconnect og backoff

Nettverksforbindelser forsvinner.

En bot må derfor kunne etablere en ny sesjon, men den skal ikke bombardere serveren med tilkoblingsforsøk.

Eksempelboten starter med en kort ventetid og øker den ved gjentatte feil:

```text
2s -> 4s -> 8s -> 16s -> 32s -> 60s
```

Dette er en enkel begrenset eksponentiell backoff.

## Ny forbindelse betyr ny registrering

Etter reconnect må klienten igjen:

```text
TCP/TLS
  -> NICK/USER
  -> vent på registrering
  -> JOIN
```

State fra den gamle socketen kan ikke bare antas å være gyldig.

## Produksjon er mer komplisert

En større klient vil blant annet måtte håndtere:

- nick-kollisjon
- server-feil og numerics
- rate limits
- SASL
- IRCv3 CAP
- flere kanaler
- ønsket state etter reconnect
- kontrollert shutdown

Den minimale boten er fundamentet, ikke slutten.
