# Permanent WeeChat eller Irssi

Nå kombinerer vi delene.

## WeeChat med tmux

```sh
ssh bruker@shell.example.net
tmux new -s irc
weechat
```

Koble WeeChat til IRC-nettverket etter klientens konfigurasjon. Når alt fungerer, detach fra tmux.

Senere:

```sh
ssh bruker@shell.example.net
tmux attach -t irc
```

## Irssi med tmux

Samme arkitektur fungerer med Irssi:

```sh
tmux new -s irssi
irssi
```

Dette viser hvorfor vi skilte arkitektur fra klientvalg tidligere i boka.

## Hva er egentlig permanent?

Det er viktig å være presis. tmux gjør ikke IRC-forbindelsen magisk permanent. Det gjør at **IRC-klientprosessen kan fortsette å kjøre uten den lokale SSH-terminalen**.

Hvis shell-serveren starter på nytt, klienten krasjer eller nettverket brytes, må klienten kunne koble seg til igjen.

Vi trenger derfor både:

- vedvarende terminalsesjon
- klientens reconnect/autoconnect
- korrekt TLS/SASL-konfigurasjon

Senere ser vi på hvordan tjenester og bouncere kan gi en enda mer driftbar modell.
