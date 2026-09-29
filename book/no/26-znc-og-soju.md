# ZNC og soju: to bouncer-modeller

Denne boka dekker både **ZNC** og **soju** fordi de representerer to nyttige måter å tenke IRC-bouncer på.

## ZNC

ZNC er en etablert IRC-bouncer med et modulsystem og lang brukshistorie. Den passer godt til å lære den tradisjonelle bouncer-modellen:

```text
IRC-klient -> ZNC -> ett eller flere IRC-nettverk
```

ZNC har også funksjoner som går langt utover den enkleste BNC-modellen.

## soju

soju er utviklet med moderne IRC og IRCv3 som en sentral del av designet. Den er særlig interessant når flere klienter/enheter, historikk og moderne protokollfunksjoner er viktige.

Arkitekturen er fortsatt gjenkjennelig:

```text
IRC-klienter -> soju -> IRC-nettverk
```

men klient/bouncer-forholdet kan utnytte moderne IRC-funksjoner bedre enn eldre «én klient bak en relay»-tankegang.

## Vi skal bygge begge

I stedet for å kåre én universell vinner bygger vi begge løsningene i labbene.

Da kan vi sammenligne:

- installasjon og drift
- konfigurasjonsmodell
- TLS
- upstream SASL
- flere nettverk
- flere klienter
- historikk/playback
- IRCv3
- backup og oppgraderinger

Leseren får dermed grunnlag for å velge ut fra sitt eget miljø.
