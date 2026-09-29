# Problemet med blokkerende recv

En IRC-forbindelse kan være stille lenge. Hvis programmet blokkerer ubegrenset i `recv()`, er det ikke nok at en signalhandler bare setter et stop-flagg: hovedløkken får kanskje aldri anledning til å lese flagget.

Dette er en lifecycle-feil, ikke bare et ytelsesproblem.

Eksempelklienten bruker nå en kort socket-timeout som polling-grense. En timeout betyr «ingen data ennå», ikke «forbindelsen er ødelagt».
