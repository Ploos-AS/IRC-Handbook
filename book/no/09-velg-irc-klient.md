# Velg IRC-klient

IRC-protokollen er uavhengig av brukergrensesnittet. Derfor kan svært forskjellige programmer koble seg til det samme nettverket.

## Fire vanlige klienttyper

**Grafiske desktop-klienter** passer godt når du ønsker vinduer, menyer, varsler og enkel konfigurasjon.

**Terminalklienter** som WeeChat og Irssi passer spesielt godt på shell-kontoer og over SSH.

**Webklienter** kjører i nettleseren og kan være praktiske når du ikke vil installere en lokal klient.

**Mobilklienter** gjør IRC tilgjengelig på telefon og nettbrett, men permanente forbindelser kan være utfordrende på mobile plattformer. En bouncer løser mye av dette.

## Hva bør en moderne klient støtte?

Se etter støtte for:

- TLS med sertifikatvalidering
- SASL
- IPv6 der det er relevant
- flere IRC-nettverk
- moderne IRCv3-funksjoner
- god håndtering av reconnect
- sikre måter å lagre credentials på
- logging dersom du ønsker det

## Klienten er utskiftbar

Det er en styrke ved IRC. Du kan begynne med en enkel grafisk klient og senere gå over til WeeChat på en shell-server uten å bytte IRC-nettverk.

Med en bouncer kan du til og med bruke flere forskjellige klienter mot den samme permanente IRC-sesjonen.

I denne boka bruker vi derfor klienten som et verktøy, ikke som selve plattformen.
