# M6.4: live ServerFeatures

M6.4 lukker skillet mellom «vi kan parse ISUPPORT» og «programmet følger ISUPPORT».

Session-laget:

1. mottar 005
2. oppdaterer `ServerFeatures`
3. bruker aktiv CASEMAPPING i meldingslogikken
4. gjør PREFIX og CHANMODES tilgjengelige som strukturerte regler

Dette er viktig interoperabilitet. IRC-nettverk er ikke identiske, og en robust klient bør lære relevante regler fra serveren i stedet for å late som alle servere er konfigurert likt.

Neste steg er å koble dette til en levende kanalmodell med NAMES-replay og dynamisk MODE-state.
