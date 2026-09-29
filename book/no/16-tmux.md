# tmux: behold terminalsesjonen

`tmux` er en terminalmultiplexer. Den lar et program fortsette å kjøre på shell-serveren selv om SSH-forbindelsen din avsluttes.

## Start en navngitt sesjon

```sh
tmux new -s irc
```

Start deretter for eksempel WeeChat:

```sh
weechat
```

Nå kjører WeeChat inne i tmux-sesjonen `irc`.

## Detach

I standardoppsettet kan du løsne klientterminalen fra tmux med prefix `Ctrl-b`, etterfulgt av `d`.

WeeChat avsluttes ikke. Det fortsetter å kjøre på serveren.

Du kan nå logge ut:

```sh
exit
```

## Attach igjen

Senere:

```sh
ssh bruker@shell.example.net
tmux attach -t irc
```

Du kommer tilbake til den samme terminalsesjonen.

## Finn sesjonene

```sh
tmux ls
```

Dette er nyttig hvis du har glemt sesjonsnavnet eller kjører flere sesjoner.

## Viktig mental modell

```text
WeeChat
   |
 tmux-sesjon        <- fortsetter på serveren
   |
 SSH-forbindelse    <- kan kobles fra
   |
din terminal
```

tmux er ikke en IRC-bouncer. Det bevarer terminalprogrammet. IRC-klienten selv forblir tilkoblet nettverket.
