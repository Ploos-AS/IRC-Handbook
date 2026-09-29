# Hva er IRC?

Internet Relay Chat (IRC) er en åpen protokoll for tekstbasert sanntidskommunikasjon. I stedet for at én leverandør eier hele tjenesten, består IRC-verdenen av mange uavhengige nettverk. Et nettverk består av én eller flere IRC-servere som samarbeider om å gi brukerne et felles sett med kanaler og samtaler.

## Den grunnleggende modellen

Når du bruker IRC, kjører du en **IRC-klient**. Klienten kobler seg til en **IRC-server**, og serveren er del av et **IRC-nettverk**. På nettverket kan du gå inn i **kanaler**, vanligvis med navn som begynner med `#`.

```text
IRC-klient -> IRC-server -> IRC-nettverk -> #kanal
```

Et **nick** er navnet du vises med. IRC har også begrepene brukernavn og host, men de er ikke det samme som nicket ditt.

## IRC er en protokoll, ikke ett nettsted

Dette skillet er viktig. IRC kan sammenlignes mer med e-post enn med en enkelt chat-tjeneste: mange klienter og serverimplementasjoner kan snakke samme protokoll. Derfor kan du bytte klient uten å bytte nettverk, og et nettverk kan drives uavhengig av andre nettverk.

## Hvorfor lære IRC i dag?

IRC er fortsatt interessant fordi systemet er enkelt nok til å forstå, samtidig som det kan bygges til en svært robust kommunikasjonsplattform. Du kan bruke en vanlig desktop-klient, ha klienten kjørende på en shell-konto, koble flere enheter gjennom en bouncer eller drifte hele infrastrukturen selv.

Denne boka begynner med vanlig IRC-bruk. Senere bygger vi videre mot:

- sikre forbindelser med TLS og SASL
- shell-kontoer og SSH
- tmux og screen
- ZNC og soju
- IRC-boter
- IRCv3
- egen IRC-server
- et permanent IRC-miljø på en VPS

Målet er ikke bare at du skal kunne *bruke* IRC. Når boka er ferdig, skal du forstå hva som skjer mellom klienten og serveren og kunne bygge din egen løsning.
