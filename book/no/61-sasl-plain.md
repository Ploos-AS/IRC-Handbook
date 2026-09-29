# SASL PLAIN

SASL PLAIN sender et base64-kodet autentiseringsfelt. Base64 er **ikke kryptering**.

Derfor skal SASL PLAIN brukes over en TLS-beskyttet forbindelse i reell drift.

Sekvensen i eksempelboten er:

```text
CAP REQ :sasl
<- CAP ... ACK :sasl
AUTHENTICATE PLAIN
<- AUTHENTICATE +
AUTHENTICATE <base64-payload>
<- 903 ...
CAP END
```

Payloaden representerer i vårt enkle eksempel:

```text
NUL + account + NUL + password
```

Ekte credentials leses fra miljøvariablene `IRC_SASL_USER` og `IRC_SASL_PASSWORD`, ikke fra Git.
