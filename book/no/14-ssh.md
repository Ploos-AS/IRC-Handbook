# SSH

SSH er den normale måten å logge inn sikkert på en moderne shell-server.

En grunnleggende tilkobling ser slik ut:

```sh
ssh bruker@shell.example.net
```

Første gang må klienten vanligvis ta stilling til serverens host key.

## Host keys betyr noe

SSH bruker serverens host key for å hjelpe deg å oppdage om du senere blir sendt til en annen maskin enn forventet.

Ikke tren deg opp til å svare ja på alle sikkerhetsadvarsler. Hvis en kjent servers nøkkel plutselig endres, undersøk hvorfor.

## SSH-nøkler

Nøkkelbasert autentisering er normalt å foretrekke fremfor gjentatt passordinnlogging.

Et moderne nøkkelpar kan for eksempel opprettes med:

```sh
ssh-keygen -t ed25519
```

Den private nøkkelen blir på klientmaskinen. Den offentlige nøkkelen kan installeres på shell-serveren.

**Del aldri den private nøkkelen.**

## authorized_keys

På serveren brukes normalt:

```text
~/.ssh/authorized_keys
```

til å angi offentlige nøkler som får logge inn på kontoen.

SSH-katalogen og filene må ha fornuftige rettigheter. Vi undersøker dette nærmere i neste kapittel.

## En shell er ikke en sikker sandkasse

Når du logger inn på en delt maskin, må du forholde deg til administratorens sikkerhetspolicy og andre brukere på systemet. Ikke anta at en tilfeldig shell-provider er et passende sted for sensitive hemmeligheter.

Senere setter vi opp vår egen server og kan kontrollere flere av disse valgene selv.
