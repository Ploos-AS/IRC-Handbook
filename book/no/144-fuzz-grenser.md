# Fuzzing har grenser

Denne harnessen er bevisst liten og bruker bare Python-standardbiblioteket. Den er ikke en erstatning for dedikerte fuzzere eller property-baserte rammeverk.

Verdien her er pedagogisk og praktisk: leseren kan se hele mekanismen, seedene er stabile, og testene kan kjøre uten ekstra avhengigheter.

Parsefeil på mutasjoner som ikke lenger er gyldige IRC-meldinger er forventet. Det interessante er at parsebare sekvenser ikke skal korrumpere state.
