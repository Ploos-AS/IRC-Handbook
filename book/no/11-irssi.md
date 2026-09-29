# Irssi

Irssi er en klassisk terminalbasert IRC-klient med sterk tilknytning til Unix- og shell-kulturen.

## Den klassiske shell-opplevelsen

Et svært vanlig mønster har vært:

```text
lokal terminal
      |
     SSH
      |
shell-server
      |
 screen/tmux
      |
    Irssi
      |
IRC-nettverk
```

Du logger inn via SSH, kobler deg til en eksisterende terminalsesjon og fortsetter der du slapp.

## Hvorfor dekke både Irssi og WeeChat?

De løser mange av de samme oppgavene, men har forskjellig brukergrensesnitt, konfigurasjon og økosystem.

Å lære begge gjør også et viktig poeng tydelig: **shell-arkitekturen er ikke bundet til én IRC-klient**.

## Kommandoer og protokoll

Når du skriver:

```text
/join #retro
```

er dette fortsatt en klientkommando. Irssi oversetter handlingen til IRC-protokollen på samme måte som andre klienter.

Dermed kan kunnskapen fra de første kapitlene brukes uavhengig av klientvalg.

## Senere lab

I shell-delen setter vi opp Irssi med TLS og SASL, kjører den under tmux/screen og tester reconnect. Deretter sammenligner vi denne modellen med en dedikert bouncer.
