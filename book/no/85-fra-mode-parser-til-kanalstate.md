# Fra MODE-parser til kanalstate

Vi har nå kjeden:

```text
005 ISUPPORT
   ↓
PREFIX + CHANMODES
   ↓
MODE-linje
   ↓
ModeChange[]
   ↓
kanaltilstand
```

Eksempelparseren stopper foreløpig ved listen av endringer. Det er bevisst.

Neste lag kan vedlikeholde en modell av:

- kanalens flaggmodes
- key/limit
- medlemsstatus per nick
- ban/exception/invite-lister

Ved å holde parsing og state separat blir begge deler enklere å teste, og replay av en protokolltranscript kan brukes til å rekonstruere kanaltilstand.
