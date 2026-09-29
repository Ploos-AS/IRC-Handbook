# M5: fra linjer til protokollplattform

Gjennom M5 har den pedagogiske klienten vokst fra enkel linjehåndtering til flere eksplisitte protokolllag:

```text
TCP/TLS
  ↓
IRC framing og parser
  ↓
numerics + ISUPPORT
  ↓
CASEMAPPING / PREFIX / CHANMODES
  ↓
MODE + ChannelState
  ↓
CTCP
  ↓
IRCv3 tags + CapabilityState
  ↓
stateful CAP/SASL negotiation
```

Poenget er ikke å konkurrere med modne IRC-biblioteker. Poenget er at leseren nå kan følge mekanismene selv og forstå hvorfor en robust klient trenger dem.

Før vi kaller eksempelklienten produksjonsklar gjenstår hardening, blant annet hemmelighetshåndtering, strengere SASL/TLS-policy og flere protokollkanter. Dette blir naturlig inngang til neste del.
