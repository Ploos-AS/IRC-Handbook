# M6.1: hardening av protokollklienten

Før eksempelboten kan nærme seg produksjonsbruk må sikkerhetsgrenser være eksplisitte.

M6.1 etablerer fire slike grenser:

- autentiseringspayloads redigeres bort fra logger
- SASL PLAIN tillates ikke uten TLS
- AUTHENTICATE chunkes etter protokollens 400-tegnsregel
- IRCv3 tag escapes dekodes i én passering

Dette er hardening, ikke nye brukerfunksjoner. Nettopp slike endringer skiller ofte en demonstrasjon fra programvare man kan begynne å stole på.

Det gjenstår fortsatt arbeid, særlig rundt responsiv socket-shutdown og ytterligere integrasjonstesting.
