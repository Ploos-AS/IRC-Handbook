# Brukere, ressurser og backup

En privat IRC-shell for én person er enkel. En shell-tjeneste med flere brukere er en helt annen sikkerhetsmodell.

## Separate brukere

Hvis flere personer skal bruke serveren, bør de ha separate Unix-kontoer. Ikke del én konto og én SSH-nøkkel mellom alle.

Da kan tilgang fjernes per bruker, og filer og prosesser får tydelig eierskap.

## Ressurser

En feilkonfigurert bot eller klient kan bruke unødvendig CPU, minne, prosesser eller diskplass. På en delt tjeneste bør ressursgrenser og overvåking derfor inngå i designet.

Dette blir spesielt viktig når vi senere diskuterer hosting av boter og bouncere.

## Hva bør sikkerhetskopieres?

For en personlig shell er de viktigste dataene ofte:

- klientkonfigurasjon
- bouncerkonfigurasjon
- scripts du selv har skrevet
- relevante logger dersom du bevisst ønsker å beholde dem
- dokumentasjon av serveroppsettet

Private nøkler og andre secrets krever særskilt behandling. Ikke kopier dem ukritisk inn i vanlige backups eller Git.

## Test restore

En backup du aldri har forsøkt å gjenopprette er bare en antakelse.

En enkel test er å gjenopprette konfigurasjonen til et separat område og kontrollere at nødvendige filer faktisk finnes.

## Mot en tjeneste

Med dette fundamentet kan vi senere utvide modellen:

```text
Debian
  +-- shell-brukere
  +-- terminalklienter
  +-- bouncere
  +-- boter
  +-- overvåking
  +-- backup
```

Da beveger vi oss fra «min IRC-shell» til en ordentlig IRC-hostingplattform.
