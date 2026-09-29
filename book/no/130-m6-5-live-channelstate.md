# M6.5: live ChannelState

Kanalmodellen er nå koblet inn i den faktiske session-løkken.

005 konfigurerer reglene. 353 bygger medlemslisten. 366 avgrenser NAMES-snapshotet, og etterfølgende MODE- og medlems-events oppdaterer samme modell.

Fake-server-integrasjonen spiller også gjennom ISUPPORT, NAMES og MODE slik at denne protokollkjeden faktisk går gjennom runtime.

Det gjenstår fortsatt detaljer før modellen kan kalles komplett, blant annet eksplisitt snapshot-generasjon, flere kanaler og mer avansert resynkronisering etter tapte events. Men den tidligere store mangelen — å ikke vite hvem som allerede var i kanalen ved join — er nå lukket.
