# 157. Vår egen kanal-livssyklus

Det er forskjell på at en annen bruker forlater en kanal og at klienten selv gjør det.

Når en annen bruker sender PART eller blir KICK-et, fjernes brukeren fra medlemslisten. Når vår egen klient sender PART eller blir KICK-et, finnes ikke lenger noen aktiv channel-session lokalt. Hele kanalmodellen skal derfor fjernes.

Tilsvarende etablerer vår egen JOIN en channel-session. Denne modellen gjør registry-et til en beskrivelse av kanalene klienten faktisk er medlem av, ikke en historikk over kanaler den tidligere har besøkt.
