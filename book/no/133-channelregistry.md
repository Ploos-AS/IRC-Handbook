# ChannelRegistry

Én IRC-tilkobling kan være medlem av flere kanaler.

`ChannelRegistry` eier derfor en separat `ChannelState` per kanal og bruker serverens CASEMAPPING for kanalnøkler.

Kanalspesifikke events som 353, 366, JOIN, PART, KICK og MODE rutes til riktig kanal. Globale brukerhendelser som NICK og QUIT spilles gjennom alle kjente kanaler.
