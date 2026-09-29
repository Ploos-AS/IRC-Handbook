# SASL PLAIN krever TLS

PLAIN beskytter ikke passordet på transportlaget. Derfor nekter eksempelkonfigurasjonen nå å bruke SASL-legitimasjon når TLS er deaktivert.

Policyen er enkel:

```text
SASL PLAIN + TLS     → tillatt
SASL PLAIN uten TLS → stopp
```

Et lokalt testoppsett bør ikke svekke produksjonspolicyen i hovedprogrammet. Testharnesser kan teste lavere protokolllag separat uten å gjøre usikker konfigurasjon til en normal kjøremodus.
