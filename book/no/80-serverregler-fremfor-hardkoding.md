# Serverregler fremfor hardkoding

Vi kan nå koble flere deler av `005 RPL_ISUPPORT` til faktisk klientoppførsel:

```text
PREFIX      -> medlemsstatus
CHANMODES   -> mode-parameterregler
CASEMAPPING -> sammenligning av nick/kanalnavn
CHANTYPES   -> hvilke prefiks som markerer kanaler
NICKLEN     -> serverens nick-grense
```

Dette er et sentralt prinsipp i robuste IRC-klienter:

**spør serveren hvilke regler den annonserer, i stedet for å late som alle IRC-nettverk er identiske.**

Neste steg er å bruke disse byggesteinene til å parse og oppdatere kanaltilstand fra faktiske `MODE`-meldinger.
