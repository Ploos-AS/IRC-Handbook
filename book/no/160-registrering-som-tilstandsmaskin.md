# Registrering som tilstandsmaskin

En IRC-klient er ikke «tilkoblet og ferdig» idet TCP-forbindelsen er opprettet. Før normal bruk må klienten gjennom en protokollsekvens: CAP-forhandling, NICK og USER, eventuell SASL-autentisering og til slutt velkomstnumerikken 001.

I den minimale boten modellerer vi denne sekvensen eksplisitt med `Registration`. Objektet har en fase som beskriver hvor i registreringen forbindelsen befinner seg. Dermed slipper vanlige meldingshandlere å gjette om en 903, 904 eller CAP ACK tilhører en aktiv registrering.

Dette er et viktig systemsprinsipp: protokolltilstand bør være eksplisitt data. Når tilstanden bare finnes implisitt i kontrollflyten, blir feil ved reconnect, forsinkede meldinger og uventet rekkefølge mye vanskeligere å oppdage og teste.

M6.13 skiller også registrering fra `SessionState`. Registration beskriver hvordan vi blir registrert. SessionState beskriver det serveren har fortalt oss om den aktive forbindelsen. ChannelRegistry beskriver observert kanaltilstand. Disse tre begrepene må ikke blandes.