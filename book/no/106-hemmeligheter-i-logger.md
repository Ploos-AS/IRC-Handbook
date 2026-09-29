# Hemmeligheter hører ikke hjemme i logger

SASL PLAIN sender en base64-kodet autentiseringspayload. Base64 er koding, ikke kryptering, og payloaden må behandles som en hemmelighet.

Eksempelboten sender fortsatt den ekte AUTHENTICATE-linjen til serveren, men logger bare:

```text
AUTHENTICATE <redacted>
```

Dette er et viktig mønster: observability skal vise at en protokollhandling skjedde uten å kopiere legitimasjon inn i terminalhistorikk, CI-logger eller loggaggregatorer.
