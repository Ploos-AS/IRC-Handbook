# ZNC: TLS og innlogging

Når IRC-klienten kobler seg til ZNC, oppretter vi en ny sikkerhetsgrense:

```text
IRC-klient
    |
 TLS + ZNC-autentisering
    |
   ZNC
    |
 upstream IRC
```

Dette er separat fra autentiseringen mellom ZNC og IRC-nettverket.

## To sett credentials

Det er nyttig å tenke:

```text
A: klient -> ZNC
   ZNC_USER + ZNC_PASSWORD

B: ZNC -> IRC-nettverk
   IRC_ACCOUNT + IRC_SECRET
```

De trenger ikke være de samme, og det er ofte bedre at de ikke er det.

## TLS mot klienten

Hvis ZNC er tilgjengelig over Internett, bør klientforbindelsen beskyttes med TLS og sertifikatet valideres.

Et offentlig DNS-navn og et sertifikat fra en vanlig betrodd CA gjør dette enklere for flere klienter.

## Firewall

Åpne bare porten du faktisk har valgt for den TLS-beskyttede ZNC-lytteren.

Dokumenter porten som en del av serverkonfigurasjonen i stedet for å anta at alle ZNC-installasjoner bruker samme verdi.

## Test lag for lag

Ved feil:

1. lytter ZNC?
2. når TCP-forbindelsen frem?
3. lykkes TLS?
4. lykkes ZNC-autentisering?
5. kobler ZNC videre til IRC?

Denne rekkefølgen er mye mer effektiv enn å endre flere ting samtidig.
