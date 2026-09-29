# CTCP framing og validering

CTCP er gammelt, lite og enkelt nok til at det er fristende å bygge strenger direkte.

Vi holder likevel framing i en egen funksjon.

`ctcp_frame()` avviser CR, LF og CTCP-delimiter i kommando/argument. Den vanlige IRC-serializeren har i tillegg sin egen CR/LF-kontroll.

Dette gir lagdeling:

```text
CTCP-data
   ↓
CTCP frame
   ↓
PRIVMSG / NOTICE
   ↓
IRC line
   ↓
TCP
```

Hvert lag kan dermed validere sine egne grenser.

Neste del går videre til moderne IRCv3 capabilities og message tags.
