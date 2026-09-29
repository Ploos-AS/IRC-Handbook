# Én eier per protokollovergang

En protokollimplementasjon blir fort skjør dersom flere deler av programmet kan reagere på den samme kontrollmeldingen. Før M6.13 kunne registreringslogikk finnes både i den generelle meldingshandleren og i CAP-forhandlingen. Da kan samme hendelse i verste fall utløse to svar eller to tilstandsoverganger.

M6.13 bruker derfor regelen **én eier per protokollovergang**. `Registration` eier registreringsrelaterte hendelser: CAP, SASL, nick-kollisjon og velkomst. Den vanlige meldingsbehandlingen trenger ikke lenger å implementere en parallell, stateless versjon av disse overgangene.

Regelen gjør også testene mer presise. En test for 433 skal teste Registration, fordi det er Registration som kjenner gjeldende nick og registreringsfase. En test for SASL-resultater skal starte den nødvendige CAP/SASL-sekvensen først. Ellers tester vi en kunstig tilstand som en virkelig klient ikke burde være i.

Dette mønsteret er nyttig langt utenfor IRC: når én komponent eier en protokolltilstand, blir invariants, logging, replay og feilhåndtering langt enklere å forstå.