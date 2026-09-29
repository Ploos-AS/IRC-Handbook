# Integrasjonstester for feilveier

Fake-serveren tester nå mer enn happy path.

Scenariene omfatter:

- vanlig registrering
- nick-kollisjon med `433`
- server `ERROR`
- SASL required, men capability mangler
- SASL required og autentisering feiler

Dette er viktig fordi en nettverksklient ofte virker fint så lenge serveren gjør nøyaktig det utvikleren forventet.

Robusthet oppstår først når uønskede, men gyldige protokollforløp også er spesifisert og testet.

Testene bruker fortsatt bare loopback og syntetiske credentials.
