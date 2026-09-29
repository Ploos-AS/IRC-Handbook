# Test fragmenterte IRC-linjer

En av de viktigste integrasjonstestene handler ikke om IRC-kommandoene i seg selv, men om TCP.

Fake-serveren sender med vilje enkelte linjer i flere writes:

```text
write #1: ":fake.example 001 handbookbot :Wel"
write #2: "come to the test server\r\n"
```

Boten må se dette som én IRC-linje.

Det samme gjøres med:

```text
:alice!u@h PRIVMSG #handbook-test :!hello
```

## Hva beviser testen?

Den demonstrerer at klienten ikke gjør den klassiske feilen:

```text
én recv() == én protokollmelding
```

I stedet er modellen:

```text
TCP bytes
   |
buffer
   |
finn LF
   |
komplett IRC-linje
   |
parser
```

Dette mønsteret er relevant langt utenfor IRC. Mange stream-baserte nettverksprotokoller krever tilsvarende framing.
