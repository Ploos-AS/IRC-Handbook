# Velge capabilities

Klienten har en liten ønskeliste:

```text
server-time
account-tag
message-tags
```

SASL legges til når legitimasjon er konfigurert.

Men ønskelisten er ikke en antakelse om serveren. Etter komplett CAP LS beregnes snittet mellom det klienten ønsker og det serveren faktisk tilbyr.

Bare dette snittet sendes i `CAP REQ`.
