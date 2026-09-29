# Timeout er ikke disconnect

Det er viktig å skille mellom tre hendelser:

- socket-timeout: ingen data i dette korte intervallet
- EOF: motparten har lukket strømmen
- socket-feil: transporten feilet

Bare de to siste beskriver at forbindelsen ikke lenger kan brukes.

Denne forskjellen hindrer en stille IRC-kanal i å utløse meningsløse reconnect-looper.
