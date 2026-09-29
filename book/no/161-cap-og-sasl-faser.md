# CAP- og SASL-faser

Ved oppstart sender boten `CAP LS 302`, `NICK` og `USER`. CAP-forhandlingen kan deretter føre til en SASL-fase dersom autentisering er konfigurert og serveren tilbyr den nødvendige capabilityen.

Poenget med fasene er ikke bare ryddigere kode. De avgrenser hvilke protokollmeldinger som har mening. En SASL-suksess eller -feil er bare en registreringsovergang når SASL faktisk pågår. En tilfeldig eller forsinket 903 skal derfor ikke flytte en forbindelse fra CAP-fasen til «registering».

Når SASL er påkrevd, behandles en autentiseringsfeil som fatal først når klienten faktisk er i SASL-fasen. Når SASL lykkes, avsluttes CAP-forhandlingen og registreringen fortsetter.

Dette gjør state-maskinen robust mot meldinger som kommer i en lovlig syntaks, men i feil protokollkontekst.