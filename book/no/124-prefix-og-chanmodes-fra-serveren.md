# PREFIX og CHANMODES fra serveren

`PREFIX` beskriver medlemsstatus som operator, half-op og voice, og hvilke prefikstegn som representerer dem.

`CHANMODES` grupperer channel modes etter parameterregler.

`ServerFeatures` eksponerer begge i ferdig parset form. Dermed finnes nå én autoritativ runtime-kilde for reglene som MODE- og kanalmodellen trenger.

Neste kobling er å la den levende `ChannelState` bruke disse verdiene direkte.
