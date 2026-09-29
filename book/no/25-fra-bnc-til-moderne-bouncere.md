# Fra BNC til moderne bouncere

Bouncere har lang historie i IRC-miljøet.

Tidlige BNC-løsninger fokuserte først og fremst på å holde en forbindelse mot IRC åpen og la brukeren koble seg videre gjennom den.

## Klassisk shell-kultur

Et typisk miljø kunne inneholde:

```text
shell-konto
  +-- screen
  +-- Irssi
  +-- BNC/psyBNC
  +-- Eggdrop
```

Dette er en viktig del av historien boka ønsker å bevare. Mange konsepter i dagens IRC-hosting kommer direkte fra denne kulturen.

## psyBNC

psyBNC ble en kjent representant for den klassiske bouncer-generasjonen. Den er nyttig å kjenne historisk fordi den viser hvordan permanente IRC-forbindelser lenge ble tilbudt fra shell-servere.

Vi bruker ikke historisk popularitet som argument for å velge gammel programvare til en moderne produksjonsserver. Sikkerhet, vedlikehold og dagens protokollstøtte må vurderes separat.

## Moderne forventninger

I dag kan vi ønske mer enn bare:

```text
hold TCP/IRC-forbindelsen åpen
```

En moderne løsning kan også håndtere:

- flere IRC-nettverk
- flere klientenheter
- meldingshistorikk
- moderne IRCv3-funksjoner
- konto-/brukeradministrasjon
- TLS
- SASL mot upstream-nettverk

Dermed har «bouncer» utviklet seg fra en enkel relay til et mer omfattende mellomlag i IRC-arkitekturen.
