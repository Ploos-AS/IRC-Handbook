# ChannelState fra ServerFeatures

`ChannelState.configure()` kopierer de relevante protokollreglene fra levende `ServerFeatures`:

- CASEMAPPING
- medlemsmodes fra PREFIX
- CHANMODES

Dermed bruker medlemsindeksen og MODE-parseren de samme reglene som serveren annonserte.

Dette er viktig fordi state som er korrekt under RFC1459-casemapping ikke nødvendigvis er korrekt under ASCII-casemapping.
