# CTCP: et protokollag inni IRC

CTCP, Client-To-Client Protocol, bruker tekstfeltet i IRC `PRIVMSG` og `NOTICE` til å bære små strukturerte meldinger.

En CTCP-frame avgrenses av byte/tegn `0x01`:

```text
\x01VERSION\x01
\x01ACTION vinker\x01
\x01PING 12345\x01
```

Dette er ikke en ny IRC-kommando på wire. Ytterst ser serveren fortsatt `PRIVMSG` eller `NOTICE`.

Minimal-klienten har nå `parse_ctcp()` og `ctcp_frame()`, slik at CTCP ikke blandes sammen med vanlig chattekst.
