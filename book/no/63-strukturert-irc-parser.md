# En strukturert IRC-parser

Minimalboten bruker nå en generell meldingsmodell:

```text
Message
  tags
  prefix
  command
  params
```

Dermed trenger ikke hver funksjon å splitte rå tekst på sin egen måte.

En melding som:

```text
@time=2026-09-29T06:00:00Z :nick!u@host PRIVMSG #kanal :hei verden
```

blir representert som strukturerte felt før botlogikken ser den.

Dette er et viktig skille mellom transport/parsing og applikasjonslogikk.
