# M6.13-kvalifisering

M6.13 kvalifiserer den eksplisitte registreringsmaskinen.

Den kvalifiserte kodecommitten er:

`00c0cee6e43ca47760d262520f21b28bf0811390`

GitHub Actions-run `36628500155` kjørte Minimal IRC bot-testene på Python 3.11, 3.12 og 3.13. Alle tre jobbene passerte. Build-run `36628500156` passerte også.

Kvalifiseringen dekker blant annet eksplisitte registreringsfaser, CAP/SASL-sekvensen, required-SASL-feil, nick-kollisjon, engangs-JOIN etter 001 og beskyttelse mot registreringshendelser i feil fase.

M6.13 avdekket også en viktig CI-lærdom. Under utviklingen ble enkelte raske filoppdateringer liggende i forskjellige commit-trees, slik at CI kunne teste eldre testinnhold enn forventet. Den endelige kandidaten ble derfor bygget atomisk fra gjeldende main-tree med en eksplisitt verifisert testblob, én ny tree og én fast-forward commit.

Qualification-recorden ligger i `docs/qualification/M6.13.md`. Senere dokumentcommits endrer ikke hvilken kodecommit som er kvalifisert.