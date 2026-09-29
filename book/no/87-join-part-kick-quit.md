# JOIN, PART, KICK og QUIT

Medlemslisten endres gjennom flere kommandoer.

`JOIN` legger avsenderen til i den aktuelle kanalen. `PART` fjerner avsenderen fra kanalen. `KICK` fjerner nicket servermeldingen peker på.

`QUIT` er annerledes: brukeren forlater IRC-forbindelsen og må derfor fjernes fra alle kanalmodeller der klienten kjenner vedkommende.

Vårt lille eksempel modellerer én kanal, men hendelsesreglene er de samme når en større klient holder en tabell med mange `ChannelState`-objekter.
