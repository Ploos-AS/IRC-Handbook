# Eggdrop: rettigheter og drift

En kanalbot kan få betydelig makt dersom den gis operatorstatus. Derfor bør rettighetene bygges gradvis.

## Start uten unødvendig makt

Test først boten som vanlig kanalmedlem.

Hvis en funksjon senere krever operatorstatus, dokumenter hvorfor.

```text
funksjon -> nødvendig rettighet
```

er bedre enn:

```text
bot -> alle rettigheter "for sikkerhets skyld"
```

## Botbrukere er ikke Unix-brukere

Eggdrops interne bruker-/rettighetsmodell må ikke forveksles med Unix-kontoen som kjører prosessen eller IRC-kontoen på nettverket.

Vi har altså flere lag:

```text
Unix service identity
        |
Eggdrop intern auth/state
        |
IRC bot account
        |
channel privileges
```

## Persistens

I et historisk shellmiljø kan Eggdrop kjøres som en langvarig brukerprosess. På egen server bør du vurdere en service manager slik at oppstart, restart og prosessidentitet blir eksplisitt.

Ikke bygg en aggressiv restart-loop. En konfigurasjonsfeil skal ikke føre til tusenvis av raske restartforsøk.

## Backup

Ta backup av nødvendig konfigurasjon og state, men behandle secrets separat og bevisst. Test restore før du antar at backupen er brukbar.
