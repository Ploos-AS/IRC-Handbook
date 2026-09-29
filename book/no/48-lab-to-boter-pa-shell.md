# Lab: to boter på IRC-shellen

Nå kjører vi Eggdrop og EnergyMech som to separate tjenester i samme labmiljø.

## Mål

```text
Debian VPS
  |
  +-- eggdrop-user -> Eggdrop ----+
  |                               |
  +-- mech-user ----> EnergyMech -+--> IRC testmiljø
```

Botene skal ikke dele Unix-identitet eller credentials bare fordi de kjører på samme server.

## Test 1: prosessisolasjon

Kontroller at hver bot kjører under forventet Unix-bruker.

Undersøk prosessene med vanlige systemverktøy og kontroller eierskap på konfigurasjonsfilene.

## Test 2: IRC-identitet

Gi botene forskjellige IRC-identiteter.

Verifiser at de kobler til med forventet nick og, når nettverket støtter det, riktig separat botkonto.

## Test 3: kanal

La begge gå inn i en kontrollert testkanal.

Start uten operatorrettigheter. Test en enkel, ufarlig respons eller statusfunksjon.

## Test 4: frakobling

Bryt testforbindelsen kontrollert eller restart test-IRC-tjenesten dersom du eier miljøet.

Observer:

- oppdager boten bruddet?
- reconnecter den?
- bruker den kontrollert retry?
- gjenoppretter den kanaltilstedeværelsen?

## Test 5: restart av vert

Etter at konfigurasjon og backup er kontrollert, test planlagt reboot av labserveren.

Målet er at botene kommer tilbake gjennom den valgte service-/oppstartsmodellen uten at noen logger inn og starter dem manuelt.

## Test 6: minste privilegium

Gi bare én bot en konkret kanalrettighet dersom labfunksjonen faktisk krever det.

Kontroller at den andre boten fortsatt kan utføre sin oppgave uten samme rettighet.

Da har vi demonstrert at botdrift handler om mer enn å få et program til å connecte.
