# Eggdrop i praksis

Eggdrop er en naturlig første praktisk bot fordi den knytter moderne drift til den klassiske IRC-shellkulturen.

## Arkitektur

```text
Debian/shell
   |
eggdrop-bruker
   |
 Eggdrop
   |
TLS/SASL der støttet
   |
IRC-nettverk
```

## Installer kontrollert

Bruk en vedlikeholdt pakke eller den offisielle prosjektkilden som passer plattformen din. Kontroller versjon, dokumentasjon og sikkerhetsstatus før produksjonsbruk.

Ikke kopier en tilfeldig gammel `eggdrop.conf` fra nettet og anta at den er riktig for dagens versjon.

## Egen bruker

På en server du administrerer bør boten kjøre med en uprivilegert identitet.

Botens filer skal eies av riktig bruker, og konfigurasjon som inneholder secrets skal ikke være lesbar for alle lokale brukere.

## Konfigurasjonen

Tenk i funksjonelle blokker:

```text
bot-identitet
IRC-server/nettverk
TLS
konto/SASL
kanaler
brukere/rettigheter
scripts/modules
logging
```

Eksakte direktiver varierer med versjon og valgte moduler. Følg dokumentasjonen for den installerte utgaven.

## Første mål

Få først boten til å:

1. starte uten konfigurasjonsfeil
2. koble sikkert til testnettverket
3. bruke forventet nick/konto
4. gå inn i én testkanal
5. svare på en ufarlig testfunksjon

Legg til kanaladministrasjon og utvidelser først etter at grunnforbindelsen er stabil.
