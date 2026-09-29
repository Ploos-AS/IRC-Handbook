# AUTHENTICATE i 400-tegns blokker

SASL-data over IRC AUTHENTICATE må deles i blokker på maksimalt 400 tegn.

`sasl_authenticate_lines()` gjør denne oppdelingen. Dersom den base64-kodede payloaden ender nøyaktig på en 400-tegns grense, sendes en ekstra:

```text
AUTHENTICATE +
```

slik at mottakeren vet at payloaden er ferdig.

Dette er et klassisk eksempel på en protokolldetalj som sjelden synes med korte testpassord, men som bør implementeres korrekt.
