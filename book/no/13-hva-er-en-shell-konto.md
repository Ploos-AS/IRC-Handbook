# Hva er en shell-konto?

En **shell-konto** er en brukerkonto på en Unix- eller Linux-maskin der du får tilgang til et kommandolinjemiljø, vanligvis over SSH.

I IRC-sammenheng har shell-kontoer historisk vært attraktive fordi programmer kan kjøre på en maskin som er tilkoblet nettet hele tiden.

## Lokal maskin og shell-server

```text
din maskin
    |
   SSH
    |
shell-server
    |
  Unix-shell
```

Etter innlogging arbeider du på shell-serveren, ikke på din lokale PC.

Kommandoen:

```sh
hostname
```

viser derfor normalt navnet på fjernmaskinen.

## Hva kan kjøre der?

Avhengig av tjenestens regler og tilgjengelig programvare kan en shell-konto brukes til blant annet:

- WeeChat eller Irssi
- tmux eller screen
- IRC-bouncere
- IRC-boter
- små scripts og verktøy

En delt shell-tjeneste er ikke det samme som en VPS. På en vanlig shell-konto har du ofte ingen root-tilgang og deler operativsystemet med andre brukere.

## Hvorfor lære dette?

Shell-kontoen lærer oss flere grunnleggende konsepter samtidig: SSH, Unix-brukere, prosesser, filrettigheter, terminalsesjoner og fjernadministrasjon.

Disse ferdighetene kan senere brukes både på en kommersiell shell-tjeneste og på vår egen Debian-baserte VPS.
