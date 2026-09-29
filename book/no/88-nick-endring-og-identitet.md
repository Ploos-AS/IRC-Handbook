# NICK-endring og identitet

Et nick kan endres mens brukeren fortsatt er i kanalen.

Når:

```text
:Bob!user@host NICK Robert
```

mottas, skal ikke medlemsstatusen forsvinne. Hvis Bob hadde voice, må Robert fortsatt ha voice etter navneendringen.

`ChannelState.rename_member()` flytter derfor medlemmet til en ny CASEMAPPING-normalisert nøkkel og beholder mode-settet.

Dette illustrerer hvorfor nick ikke bør behandles som en permanent identifikator.
