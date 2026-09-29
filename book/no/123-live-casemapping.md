# Live CASEMAPPING

IRC-navn kan ikke alltid sammenlignes med vanlig Unicode- eller ASCII-lowercase.

Når serveren annonserer:

```text
CASEMAPPING=ascii
```

skal for eksempel `[` og `{` ikke behandles som samme tegn. Med RFC1459-casemapping kan de være ekvivalente.

Runtime bruker nå `ServerFeatures.casemapping` når den avgjør om en PRIVMSG eller CTCP er adressert direkte til botens nick.

En ukjent CASEMAPPING-verdi faller tilbake til `rfc1459` i det pedagogiske eksemplet i stedet for å krasje sesjonen.
