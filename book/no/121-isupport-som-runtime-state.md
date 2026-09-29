# ISUPPORT som runtime-state

Numeric 005, RPL_ISUPPORT, beskriver egenskaper ved IRC-serveren. Det holder ikke å kunne parse linjen hvis resten av klienten fortsatt bruker hardkodede antakelser.

Eksempelklienten har derfor fått `ServerFeatures`. Hver 005-melding oppdaterer samme state gjennom hele forbindelsen.

Serverens annonserte regler blir dermed data klienten faktisk kan bruke.
