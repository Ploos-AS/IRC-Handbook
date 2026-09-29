# Feilklasser og policy

Eksempelklienten skiller nå mellom flere utfall.

`AuthenticationError` er en policyfeil og avslutter programmet når autentisering er påkrevd. `ServerError`, `ConnectionClosed`, socket-feil og TLS-feil kan gå gjennom reconnect/backoff. Lokal shutdown returnerer et eksplisitt stopp-resultat og skal ikke reconnecte.

Klassifisering gjør hovedløkken enklere: den trenger ikke gjette årsaken ut fra tekstmeldinger.
