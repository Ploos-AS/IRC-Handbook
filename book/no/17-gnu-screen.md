# GNU Screen: den klassiske løsningen

Før tmux ble vanlig, var GNU Screen en svært utbredt måte å holde terminalprogrammer kjørende på shell-servere. Screen er derfor en viktig del av IRC-shellens historie.

## Start en sesjon

```sh
screen -S irc
```

Start deretter Irssi eller WeeChat:

```sh
irssi
```

## Detach

Standardsekvensen er `Ctrl-a`, deretter `d`.

Programmet fortsetter i Screen-sesjonen.

## Finn og gjenoppta

```sh
screen -ls
screen -r irc
```

På eldre shell-tjenester vil du ofte møte Screen i dokumentasjon og eksisterende brukeroppsett.

## Screen eller tmux?

Begge kan løse vårt grunnproblem:

```text
SSH kobles fra
      |
      X
      |
terminalmultiplexer -> IRC-klient fortsetter
```

I denne boka bruker vi hovedsakelig tmux i nye oppsett, men lærer Screen godt nok til å forstå og bruke klassiske shell-miljøer.
