# End-to-end-test av minimalboten

Hele testsettet kan kjøres med:

```sh
cd examples/minimal-bot
./run_tests.sh
```

eller:

```sh
python3 -m unittest -v
```

Testpakken inneholder nå to nivåer.

## Nivå 1: deterministiske unit-tester

Disse tester blant annet:

```text
IRC line -> responses
```

uten socket.

## Nivå 2: lokal integrasjonstest

Denne starter en ekte TCP-listener på loopback og kjører botens vanlige `run_session()` mot den.

Dermed tester vi samme kodevei som en virkelig forbindelse bruker:

```text
socket
 -> recv
 -> framing
 -> parser/state
 -> response
 -> send
```

## Transcript som kontrakt

Fake-serveren registrerer hva boten faktisk sender og sammenligner det med forventet sekvens:

```text
NICK handbookbot
USER handbookbot 0 * :IRC Handbook Bot
JOIN #handbook-test
PONG :integration-token
PRIVMSG #handbook-test :Hello, alice!
```

Dette gjør protokolloppførselen synlig og enkel å feilsøke.

Neste steg er å koble disse testene til CI og deretter utvide klienten med IRCv3 CAP og SASL uten å miste den deterministiske testmodellen.
