# M4 oppsummering: fra botbruker til protokollklient

Vi startet med etablerte boter og endte med vår egen lille IRC-klient.

Gjennom M4 har vi sett:

- klassiske og moderne boter
- Eggdrop, EnergyMech, Dancer og Sopel
- plugin-modellen
- TCP og line framing
- strukturert IRC-parsing
- PING/PONG, NICK, USER, JOIN og PRIVMSG
- IRCv3 CAP
- SASL PLAIN
- optional og required SASL-policy
- nick-kollisjon og server ERROR
- lokal fake IRC-server
- happy-path- og failure-path-tester
- graceful shutdown
- deterministisk reconnect-backoff

Eksempelboten er med vilje fortsatt liten. Verdien er at leseren kan følge hele forbindelsen fra socket til botkommando.

I M5 flyttes fokuset fra «bygg en bot» til IRC-protokollen i dybden: grammatikk, numerics, modes, ISUPPORT, CTCP, capability negotiation og moderne IRCv3-semantikk.
