# En lokal fake IRC-server

Unit-testene våre kan teste parseren uten socket. Nå tester vi også transportlaget.

Repoet inneholder en liten fake IRC-server i:

```text
examples/minimal-bot/test_integration.py
```

Den lytter bare på loopback og brukes kun som testmotpart.

## Testsekvens

```text
bot                         fake server
 |                               |
 | NICK handbookbot              |
 | USER ...                      |
 |------------------------------>|
 |                               |
 |             001 Welcome       |
 |<------------------------------|
 | JOIN #handbook-test           |
 |------------------------------>|
 |             PING :token       |
 |<------------------------------|
 | PONG :token                   |
 |------------------------------>|
 |      PRIVMSG ... :!hello      |
 |<------------------------------|
 | PRIVMSG ... :Hello, alice!    |
 |------------------------------>|
```

Når fake-serveren lukker forbindelsen avsluttes den enkelte `run_session()`.

## Hvorfor loopback?

Integrasjonstesten bruker bevisst ukryptert TCP, men bare mot `127.0.0.1` på en tilfeldig lokal port.

Det er ikke en anbefaling om plaintext IRC over Internett. Det gjør bare protokolltesten liten og deterministisk. Produksjonsforbindelsen bruker fortsatt TLS som standard.
