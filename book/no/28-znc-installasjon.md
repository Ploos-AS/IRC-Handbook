# ZNC på Debian

Nå bygger vi vår første dedikerte bouncer.

## Installer

På Debian kan ZNC installeres fra distribusjonens pakker:

```sh
sudo apt update
sudo apt install znc
```

Kontroller alltid hvilken versjon Debian-utgaven din leverer og hvilke sikkerhetsoppdateringer som er tilgjengelige.

## Ikke kjør som root

Bounceren skal kjøre med en egen, uprivilegert identitet. På en personlig server kan dette være en dedikert ZNC-bruker; på en større tjeneste må bruker- og servicearkitekturen planlegges mer systematisk.

Poenget er:

```text
root
  |
  +-- administrerer systemet

znc-bruker
  |
  +-- kjører ZNC
```

## Først privat, så eksponert

En god arbeidsrekkefølge er:

1. installer ZNC
2. opprett konfigurasjonen
3. test at prosessen starter
4. test klienttilkobling fra et kontrollert miljø
5. konfigurer TLS
6. åpne bare den nødvendige lytterporten
7. test utenfra

Ikke åpne en tilfeldig port i brannmuren før du vet hvilken tjeneste som skal lytte der og hvordan den autentiserer klientene.

## Konfigurasjonsveiviser

ZNC leverer verktøy for å opprette grunnkonfigurasjon. Dialog og detaljer kan variere mellom versjoner, så følg den installerte versjonens dokumentasjon og hjelptekst.

Ikke legg ekte ZNC-passord eller IRC-passord inn i bokas eksempelrepository.
