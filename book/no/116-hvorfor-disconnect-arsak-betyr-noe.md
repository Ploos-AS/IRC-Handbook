# Hvorfor disconnect-årsak betyr noe

En IRC-sesjon kan slutte av svært forskjellige grunner: lokal shutdown, ren EOF, serverens ERROR, transportfeil eller autentiseringspolicy.

Hvis alle behandles som «run_session returnerte», mister reconnect-laget informasjonen det trenger.

Eksempelklienten har derfor fått eksplisitt `ConnectionClosed` for EOF og `SessionResult` for kontrollert lokal avslutning.
