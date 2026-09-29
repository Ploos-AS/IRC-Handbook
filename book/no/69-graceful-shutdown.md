# Graceful shutdown

En langlivet IRC-klient bør kunne avsluttes kontrollert.

Minimalboten fanger nå `SIGINT` og `SIGTERM` gjennom et lite stoppsignal. Når sesjonen får anledning til å avslutte sender den:

```text
QUIT :Shutting down
```

før socketen lukkes.

Dette er spesielt nyttig når boten kjøres under systemd eller en container-runtime som først sender et termineringssignal.

Stopptilstanden ligger utenfor protokollparseren. Dermed kan parseren fortsatt være deterministisk og enkel å teste.
