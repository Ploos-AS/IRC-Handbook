# Nicks, identitet og modes

Et nick er den mest synlige delen av IRC-identiteten din, men det er ikke hele identiteten.

## Nick

Du kan vanligvis endre nick med:

```text
/nick NyttNick
```

På klassisk IRC er et nick i utgangspunktet knyttet til den aktive forbindelsen. Moderne nettverk tilbyr ofte kontoer og tjenester som gjør identiteten mer varig. Det kommer vi tilbake til i kapitlene om kontoer, SASL og NickServ.

## WHOIS

En av de viktigste kommandoene for å undersøke en IRC-bruker er:

```text
/whois Ada
```

Klienten presenterer informasjon serveren sender tilbake. Det kan blant annet omfatte nick, bruker/host, konto, server og kanaler, avhengig av nettverkets regler og personverninnstillinger.

## Modes

IRC bruker **modes** for å representere mange innstillinger. De finnes både for brukere og kanaler.

En kanal kan for eksempel ha moduser som påvirker hvem som kan komme inn eller hvem som kan sende meldinger. Medlemmer kan også ha statusmoduser.

Et velkjent eksempel er operatorstatus, ofte vist med `@`:

```text
@Ada
 Bob
 Carol
```

Det betyr ikke at Ada administrerer hele IRC-nettverket. Det betyr normalt at Ada har operatorprivilegier i den aktuelle kanalen.

## Kanaloperator og IRC-operatør

Disse må ikke blandes:

**Kanaloperator (channel operator)** har utvidede rettigheter i en bestemt kanal.

**IRC-operatør (IRC operator / IRCop)** har administrative oppgaver på selve IRC-nettverket.

Begrepene høres like ut, men rollene er svært forskjellige.

## MODE-kommandoen

På protokollnivå representeres endringer med `MODE`. Klienter skjuler ofte detaljene bak menyer og kommandoer.

Senere skal vi lese slike meldinger direkte:

```text
MODE #retro +o Ada
```

Det illustrerer et viktig prinsipp i boka: først lærer vi funksjonen som IRC-bruker, deretter ser vi hvordan den uttrykkes på protokollnivå.
