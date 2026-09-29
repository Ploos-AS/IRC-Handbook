# Egen IRC-shell på Debian

En liten VPS gir deg muligheten til å bygge din egen IRC-shell uten å være administrator på en delt shell-tjeneste.

I boka bruker vi Debian som referansesystem.

## Målarkitektur

```text
Laptop
  |
 SSH
  |
Debian VPS
  |
  +-- tmux
  |    +-- WeeChat/Irssi
  |
  +-- senere: bouncer
  |
  +-- senere: bots
```

Hold operativsystemet og tjenestene oppdatert, og installer bare det du faktisk trenger.

Et grunnleggende klientmiljø kan inneholde:

```sh
sudo apt update
sudo apt install tmux weechat irssi
```

Pakkenavn og tilgjengelige versjoner kan variere mellom Debian-utgaver. Kontroller alltid den utgaven du faktisk bruker.

## Ikke kjør IRC-klienten som root

Lag eller bruk en vanlig Unix-bruker for IRC-arbeidet. Root-kontoen skal ikke være den daglige IRC-identiteten.

Dette begrenser skadeomfanget dersom et program eller script får problemer.

## Begynn enkelt

Første mål er ikke å installere alt på én gang. Få denne kjeden stabil først:

```text
SSH -> vanlig bruker -> tmux -> IRC-klient
```

Når den er forstått og testet, kan bouncere og boter legges til som separate komponenter.
