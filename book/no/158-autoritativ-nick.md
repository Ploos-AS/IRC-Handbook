# 158. Autoritativ current nick

Nicket vi ber om er ikke nødvendigvis nicket sessionen ender med å bruke.

Ved registrering kan nick-collisions eller annen serverlogikk påvirke identiteten. Etter vellykket registrering inneholder numerisk `001` nicket serveren faktisk kjenner klienten som.

M6.12 bruker derfor nick-parameteren i `001` som autoritativ current nick. Senere NICK-hendelser oppdaterer den videre.

Dette er viktig for å kjenne igjen vår egen JOIN, PART og KICK, og for å avgjøre om en PRIVMSG er rettet direkte til klienten.
