# Bot-sikkerhet og identitet

En bot er programvare som mottar data fra et nettverk og kan reagere automatisk. Det gjør sikkerhetsgrensene viktige.

## Egen IRC-identitet

Bruk en egen botkonto når nettverket støtter kontoer:

```text
personkonto != botkonto
```

Da kan botens tilgang fjernes uten å påvirke menneskets konto.

## Egen Unix-identitet

På en server bør en bot normalt ikke kjøre som root.

For flere tjenester er en ryddig modell:

```text
znc-user       -> ZNC
soju-user      -> soju
eggdrop-user   -> Eggdrop
mybot-user     -> egen bot
```

Hvor langt separasjonen skal gå avhenger av miljøet, men privilegier bør være bevisste.

## Secrets

IRC-passord, SASL-hemmeligheter, tokens og private nøkler skal ikke ligge i Git.

Konfigurasjonsfiler som inneholder hemmeligheter må ha passende filrettigheter og inngå i en bevisst backup-policy.

## Ikke stol på kanaltekst

Tekst fra IRC er input fra andre brukere.

Hvis en bot mottar:

```text
!weather Oslo
```

skal argumentet behandles som data, ikke som en shell-kommando som ukritisk settes inn i `sh -c`.

Samme prinsipp gjelder filnavn, URL-er, nick og meldinger.

## Minste privilegium

Gi boten bare:

- nødvendige kanalmoduser
- nødvendige filer
- nødvendige nettverkstilganger
- nødvendige API-rettigheter

En værbot trenger for eksempel normalt ikke operatørstatus i kanalen.
