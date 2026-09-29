# Persistens, historikk og multiclient

Tre egenskaper blandes ofte sammen når bouncere diskuteres.

## 1. Persistent upstream-forbindelse

Bounceren kan fortsette å være koblet til IRC-nettverket når klienten din forsvinner.

```text
Klient --X
          Bouncer -------- IRC
```

Dette er den klassiske bouncer-egenskapen.

## 2. Historikk eller playback

En bouncer kan lagre meldinger mens klienten er borte og presentere dem når klienten kommer tilbake.

Hvordan dette fungerer varierer mellom produkter og protokollfunksjoner. «Bouncer» betyr derfor ikke automatisk «ubegrenset historikk».

Historikk har også personvernkonsekvenser: lagrede samtaler blir data som må sikres, begrenses og eventuelt slettes.

## 3. Flere klienter samtidig

En moderne bruker kan ha:

```text
desktop
laptop
telefon
tablet
```

koblet mot samme bouncer.

Dette krever mer enn bare å holde én upstream-forbindelse åpen. Klientene trenger en konsistent forståelse av samtaler, status og historikk.

Moderne IRCv3-funksjoner gjør denne modellen langt bedre enn det som var mulig med en helt enkel klassisk BNC.

## Tenk lag

Når vi senere feilsøker, spør vi alltid hvilket lag problemet tilhører:

```text
IRC-klient
    |
klient <-> bouncer
    |
bouncerens state/history
    |
bouncer <-> upstream
    |
IRC-nettverk
```

Denne modellen er en av de viktigste feilsøkingsferdighetene i resten av boka.
