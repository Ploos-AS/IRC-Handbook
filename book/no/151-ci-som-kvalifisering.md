# 151. CI som kvalifisering

En commit er ikke det samme som en bestått test.

I M6.10 lot vi derfor GitHub Actions være den eksterne kvalifiseringsmekanismen for eksempelboten. Matrisen kjører Python 3.11, 3.12 og 3.13 og må være grønn på alle tre før milepælen får status PASS.

Dette viste seg å være viktig: den første virkelige kjøringen fant regresjoner som ikke skulle skjules bak en antakelse om at testene sannsynligvis passerte.

Prinsippet er enkelt: **observer resultatet før du erklærer PASS**.
