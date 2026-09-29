# server-time, account, msgid og batch

`server-time` gjør det mulig å motta serverens tidsstempel for en hendelse i stedet for å bruke tidspunktet den lokale klienten tilfeldigvis mottok meldingen.

Account-relaterte tags kan knytte hendelsen til en autentisert konto. `msgid` kan gi en melding en identifikator. `batch` knytter meldingen til en IRCv3 batch-kontekst.

Disse feltene har ulike capabilities og semantikk; tag-navnet alene betyr ikke at klienten automatisk har forhandlet hele funksjonen.

Designregelen er derfor:

```text
CAP state bestemmer hva vi har avtalt
message tags beskriver metadata på den konkrete hendelsen
```

Neste steg er å gjøre CAP-forhandlingen i selve sesjonen stateful, slik at ønskede IRCv3-capabilities kan velges systematisk sammen med SASL.
