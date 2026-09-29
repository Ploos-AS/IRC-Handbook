# Nettverk, servere og kanaler

Når en IRC-klient viser en kanal med noen titalls brukere, er det lett å tenke på IRC som ett enkelt program. I virkeligheten er flere lag involvert.

## IRC-nettverket

Et **IRC-nettverk** er den logiske tjenesten brukerne kobler seg til. Nettverket kan bestå av flere servere som utveksler informasjon om brukere, kanaler og meldinger.

Du kobler vanligvis til et vertsnavn nettverket anbefaler, ikke til en tilfeldig intern server:

```text
Klient
  |
  v
irc.example.net
  |
  +---- server A
  +---- server B
  +---- server C
```

For brukeren oppleves dette som ett nettverk.

## Serveren

IRC-serveren tar imot klientforbindelsen, registrerer klienten og formidler IRC-meldinger. Servere i samme nettverk synkroniserer nødvendig tilstand med hverandre.

Dette gir en viktig forskjell:

- **server** er maskinen/programmet du er koblet til
- **nettverk** er IRC-miljøet serveren tilhører

## Kanaler

En **kanal** samler flere brukere i samme samtale. Tradisjonelle kanalnavn begynner ofte med `#`:

```text
#linux
#retro
#programming
```

Når du skriver:

```text
/join #retro
```

ber klienten serveren om å melde deg inn i kanalen.

En bruker kan være medlem av mange kanaler samtidig.

## Kanaltilstand

En kanal er mer enn meldinger. Serveren holder blant annet rede på:

- hvilke brukere som er i kanalen
- kanalens topic
- kanalmoduser
- operatorstatus og andre medlemsmoduser
- eventuelle invitasjoner eller ban-lister

Den nøyaktige funksjonaliteten varierer mellom nettverk og serverprogramvare.

## Nettverk er separate verdener

Nicket `Ada` på ett IRC-nettverk er ikke automatisk den samme identiteten som `Ada` på et annet. Kanalen `#retro` på to forskjellige nettverk er også to forskjellige kanaler.

En bouncer kan senere gjøre det praktisk å være koblet til flere slike nettverk samtidig.
