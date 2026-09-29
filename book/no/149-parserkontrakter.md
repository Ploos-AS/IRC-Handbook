# Parserkontrakter

En robust parser trenger ikke akseptere alt. Den trenger forutsigbare grenser.

Målet er at ugyldig struktur enten gir en kontrollert `ValueError` eller ignoreres av et eksplisitt høyere lag. Parseren skal ikke forsøke å «reparere» tvetydig protokollinput på skjulte måter.

Transcript-fuzzingen fra M6.8 gjør slike kontrakter spesielt verdifulle.
