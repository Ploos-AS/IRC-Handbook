# Mot en permanent IRC-identitet

Vi har nå tre separate konsepter:

1. **forbindelsen** — klientens aktive forbindelse til en server
2. **nicket** — navnet andre ser
3. **kontoen** — identiteten nettverket kan autentisere

Det gjør det lettere å forstå hvorfor en bouncer er nyttig.

## Uten bouncer

```text
Laptop ----> IRC-nettverk
```

Når klienten kobles fra, forsvinner forbindelsen. Hva som ellers bevares av konto, historikk og kanaler avhenger av nettverket.

## Med bouncer

```text
Laptop ----+
           |
Telefon ---+--> Bouncer ----> IRC-nettverk
           |
Tablet ----+
```

Bounceren kan beholde forbindelsen mot IRC-nettverket mens klientene dine kommer og går.

Dette gir oss fire lag å holde fra hverandre:

```text
person -> klient -> bouncer -> IRC-nettverk
```

Autentisering kan foregå på mer enn ett av disse grensene. Klienten kan autentisere mot bounceren, mens bounceren autentiserer mot IRC-nettverkets konto.

## Hvor kommer shell-kontoen inn?

En klassisk løsning var å logge inn på en Unix-maskin via SSH og la en terminalbasert IRC-klient kjøre der kontinuerlig:

```text
Laptop -> SSH -> shell-server -> IRC-klient -> IRC-nettverk
```

Med `screen` eller `tmux` kunne man koble fra terminalen uten å avslutte IRC-klienten.

Senere skal vi bygge både denne klassiske modellen og den moderne bouncer-modellen. Da blir det tydelig hvorfor shell-kontoer, ZNC og soju løser beslektede, men ikke identiske problemer.
