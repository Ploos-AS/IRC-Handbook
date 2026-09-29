# Lab: overlev et SSH-brudd

Denne labben demonstrerer hvorfor tmux brukes.

## 1. Koble til

```sh
ssh bruker@shell.example.net
```

## 2. Start tmux

```sh
tmux new -s irc-lab
```

## 3. Start klienten

```sh
weechat
```

Koble til et IRC-nettverk og gå inn i en testkanal du har lov til å bruke.

## 4. Detach

Bruk tmux-prefix `Ctrl-b`, deretter `d`.

Kontroller:

```sh
tmux ls
```

## 5. Avslutt SSH

```sh
exit
```

## 6. Koble til igjen

```sh
ssh bruker@shell.example.net
tmux attach -t irc-lab
```

WeeChat skal fortsatt kjøre.

## 7. Test et reelt nettverksbrudd

Gjenta labben, men la den lokale SSH-forbindelsen falle bort uten å avslutte WeeChat eller tmux manuelt. Koble deretter inn igjen og attach sesjonen.

## Hva beviste vi?

Vi demonstrerte skillet mellom:

```text
lokal SSH-transport
```

og:

```text
fjern prosess + IRC-forbindelse
```

Dette er kjernen i den klassiske IRC-shellmodellen.

## Rydd opp

Når labben er ferdig og klienten er avsluttet, kan en gjenværende tmux-sesjon termineres kontrollert. Ikke drep sesjoner du fortsatt bruker.
