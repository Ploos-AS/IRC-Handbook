# IRCv3 message tags

IRCv3 message tags står først på IRC-linjen og begynner med `@`.

Tags kan bære metadata uten å endre selve kommandoen:

```text
@tag=value;flag :prefix COMMAND param :trailing
```

Parseren støtter tags med og uten verdi og dekoder de grunnleggende escape-sekvensene.

Botkommandoen `!hello` virker derfor også når en server legger IRCv3-tags foran `PRIVMSG`.

Dette viser hvorfor protokollparseren bør være et eget lag.
