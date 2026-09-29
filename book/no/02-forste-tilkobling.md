# Din første IRC-tilkobling

For å bruke IRC trenger du i utgangspunktet bare tre ting: et IRC-nettverk, en klient og et nick.

## Velg en klient

Det finnes grafiske klienter, terminalklienter, mobilklienter og webklienter. Senere sammenligner vi dem grundig. I starten er det viktigere å lære modellen enn å velge den perfekte klienten.

Klienten trenger vanligvis:

- serveradresse
- port
- TLS av/på
- ønsket nick
- eventuelt konto og SASL-passord

Bruk TLS når nettverket tilbyr det.

## Når forbindelsen opprettes

Klienten åpner en forbindelse til serveren og registrerer identiteten din. Serveren svarer med velkomstmeldinger og informasjon om nettverket og funksjonene den støtter.

Etter tilkobling kan du gå inn i en kanal:

```text
/join #kanal
```

Send vanlig tekst i kanalvinduet for å snakke med de andre deltakerne.

## Noen kommandoer du bør kunne

```text
/join #kanal
/part #kanal
/nick NyttNick
/msg Nick Hei!
/whois Nick
/me tester IRC
/quit
```

Linjer som starter med `/` tolkes normalt av klienten som kommandoer. Vanlig tekst sendes som en melding til det aktive samtalevinduet.

## Kanal og privat samtale

En kanal er et felles samtalerom. En privat melding sendes direkte til et nick:

```text
/msg Ada Hei!
```

Mange klienter åpner da et eget samtalevindu.

## Første viktige vane

Ikke tenk på IRC-vinduet som selve IRC. Klienten er bare brukergrensesnittet. Under ligger en tekstprotokoll mellom klient og server. Senere skal vi se de faktiske meldingene på forbindelsen og skrive en minimal klient/bot selv.
