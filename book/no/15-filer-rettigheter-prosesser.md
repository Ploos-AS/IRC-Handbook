# Filer, rettigheter og prosesser

For å bruke en shell-konto trygt bør du forstå tre Unix-konsepter: hjemmekatalogen, filrettigheter og prosesser.

## Hjemmekatalogen

Etter innlogging befinner du deg ofte i hjemmekatalogen din:

```sh
pwd
ls -la
```

Konfigurasjonsfiler ligger ofte her eller i skjulte kataloger under hjemmekatalogen.

## Filrettigheter

Kommandoen:

```sh
ls -l
```

viser blant annet Unix-rettigheter.

For hemmelige eller private filer ønsker vi normalt ikke at andre lokale brukere skal kunne lese dem.

Et eksempel:

```sh
chmod 600 privat-fil
```

betyr at eieren får lese- og skriverettighet, mens gruppe og andre ikke får tilgang gjennom disse mode-bitene.

Ikke bruk `chmod 777` som universalløsning på permission-problemer.

## Prosesser

Når du starter:

```sh
weechat
```

kjører WeeChat som en prosess under brukerkontoen din.

Du kan undersøke egne prosesser med verktøy som:

```sh
ps
ps -u "$USER"
```

Når SSH-terminalen forsvinner, kan programmer knyttet direkte til terminalsesjonen også avsluttes eller miste terminalen.

Det er nettopp problemet terminalmultiplexere som **tmux** og **screen** hjelper oss å løse.

## Prinsippet

Vi vil ende med:

```text
SSH-forbindelse
      |
     tmux
      |
   WeeChat
      |
IRC-nettverk
```

SSH-forbindelsen kan forsvinne mens tmux-sesjonen og WeeChat fortsetter på serveren.
