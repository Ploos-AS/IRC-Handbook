# IRCv3 message tags

Message tags står foran resten av IRC-meldingen:

```text
@time=...;account=alice;msgid=abc :alice!u@h PRIVMSG #c :Hei
```

Parseren vår har støttet generelle tags en stund. Nå eksponerer `message_metadata()` noen sentrale metadatafelt eksplisitt:

- `time`
- `account`
- `msgid`
- `batch`

Fravær av et tag er normalt. Applikasjonskode må derfor ikke anta at metadata alltid finnes.
