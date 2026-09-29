# Hva er en IRC-bouncer?

En IRC-bouncer, ofte forkortet **BNC**, står mellom IRC-klienten din og IRC-nettverket.

Uten bouncer:

```text
Klient -> IRC-server
```

Med bouncer:

```text
Klient -> Bouncer -> IRC-server
```

Bounceren opptrer som en IRC-server sett fra klienten og som en IRC-klient sett fra nettverket.

## Hvorfor bruke en?

Den viktigste egenskapen er at forbindelsen mot IRC-nettverket kan fortsette selv når din lokale klient er frakoblet.

Det gjør blant annet følgende mulig:

- permanent tilstedeværelse på IRC
- reconnect uten å etablere hele IRC-sesjonen på nytt
- flere lokale enheter
- sentral konfigurasjon av nettverk
- historikk/playback i løsninger som støtter det

## Bouncer og shell er forskjellige modeller

Med shell:

```text
Laptop -> SSH -> tmux -> WeeChat -> IRC
```

fjernstyrer du i praksis klienten som kjører på serveren.

Med bouncer:

```text
Laptop -> lokal IRC-klient -> Bouncer -> IRC
```

bruker du fortsatt din lokale klient.

Det er en grunnleggende arkitekturforskjell.

## Flere enheter

```text
Desktop ---+
Laptop ----+--> Bouncer --> IRC-nettverk
Telefon ---+
```

Hvor godt samtidige klienter fungerer avhenger av bouncerens arkitektur og funksjoner. Dette skal vi undersøke konkret i ZNC- og soju-kapitlene.
