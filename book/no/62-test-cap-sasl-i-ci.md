# Test CAP og SASL i CI

Fake IRC-serveren har nå et eget SASL-scenario.

Den verifiserer hele sekvensen:

```text
CAP LS 302
NICK
USER
<- CAP LS :... sasl
CAP REQ :sasl
<- CAP ACK :sasl
AUTHENTICATE PLAIN
<- AUTHENTICATE +
AUTHENTICATE <test-payload>
<- 903
CAP END
<- 001
JOIN
```

Testkontoen heter bare `acct` med den syntetiske verdien `secret`. Den brukes aldri mot et eksternt system.

GitHub Actions kjører unit- og integrasjonstestene uten nettverkstilkobling til offentlig IRC og uten repository secrets.

Workflowen tester flere støttede Python-versjoner slik at bokas eksempel ikke bare fungerer på én utviklermaskin.
