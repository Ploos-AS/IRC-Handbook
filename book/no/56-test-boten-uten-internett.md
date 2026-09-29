# Test boten uten Internett

Protokollkode bør kunne testes uten å koble CI til et offentlig IRC-nettverk.

Repoet inneholder derfor unit-tester for den deterministiske kjernen:

```sh
cd examples/minimal-bot
python3 -m unittest -v
```

Testene kontrollerer blant annet:

- CRLF-encoding
- avvisning av line injection
- `PING` -> `PONG`
- `001` -> `JOIN`
- `!hello` i kanal
- `!hello` som privatmelding
- at vanlig tekst ignoreres
- parsing av `PRIVMSG`

## Hvorfor dette er viktig

Socket og TLS er I/O. Beslutningen:

```text
IRC-linje -> null eller flere svarlinjer
```

er derimot gjort som en liten deterministisk funksjon.

Dermed kan mesteparten av protokolloppførselen testes raskt og reproducerbart.

Neste steg er en lokal fake IRC-server som tester selve socket-framingen og en hel registreringssesjon uten offentlig nettverk.
