# Kontrollert QUIT

Når lokal shutdown er forespurt forsøker klienten å sende:

```text
QUIT :Shutting down
```

før socketen lukkes.

Dette er best effort. Hvis forbindelsen allerede er borte, skal en feil under QUIT ikke hindre prosessen i å avslutte.

Graceful shutdown betyr derfor «forsøk protokollmessig avslutning», ikke «bli hengende til serveren garanterer at den mottok den».
