# Responsiv shutdown

Receive-løkken sjekker stop-flagget mellom korte ventefaser.

Dermed kan SIGINT eller SIGTERM avslutte en helt stille IRC-sesjon uten å vente på at serveren sender neste melding.

Flyten er:

```text
recv med kort timeout
       ↓
ingen data
       ↓
sjekk stop-flagg
       ↓
fortsett eller avslutt
```

Timeout brukes altså som en kontrollmekanisme, ikke som en reconnect-trigger.
