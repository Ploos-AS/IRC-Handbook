# Transcript replay

Når parsing og state er deterministiske kan vi mate inn et lagret IRC-transcript:

```text
JOIN
JOIN
MODE +ov
NICK
PART
...
```

og rekonstruere kanalmodellen steg for steg.

Dette er svært nyttig for testing. Vi trenger ikke koble oss til et offentlig IRC-nettverk for å teste medlemslogikk.

Det åpner også for større fixture-baserte tester senere: kjente inputlinjer kan ha et forventet state-snapshot som fasit.

Neste steg er å se på CTCP og meldinger som bruker PRIVMSG/NOTICE som transport for et lite sekundært protokollag.
