# Hendelser i feil fase

Nettverksprogrammer må tåle mer enn den forventede «happy path». Meldinger kan være forsinket, duplisert eller komme etter at klienten allerede har gått videre til en ny fase. Derfor tester vi ikke bare hva Registration gjør med riktige meldinger, men også hva den **ikke** skal gjøre.

Et viktig eksempel er en sen CAP ACK etter at 001 allerede har gjort klienten registrert. Den skal ikke åpne CAP-forhandlingen igjen og må aldri føre til en ny JOIN. På samme måte er en 903 uten aktiv SASL inert; den skal ikke late som en autentisering nettopp ble fullført.

Dette gir oss en nyttig invariant:

> En hendelse som ikke er gyldig i gjeldende fase skal ikke flytte state-maskinen bakover eller gjenta en allerede fullført sideeffekt.

JOIN er en slik sideeffekt. M6.13 sørger for at velkomsten kan utløse den én gang, mens senere eller dupliserte registreringshendelser ikke kan produsere en ekstra JOIN.

Når vi senere bygger mer avansert reconnect- og medlemskapspolitikk, er dette skillet avgjørende: registreringsmaskinen bestemmer når registreringen er ferdig; medlemskapssystemet bestemmer hva vi ønsker å gjøre etterpå.