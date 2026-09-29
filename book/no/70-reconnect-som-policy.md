# Reconnect som egen policy

Reconnect-backoff er nå en separat `Backoff`-komponent.

Standardsekvensen er:

```text
2 -> 4 -> 8 -> 16 -> 32 -> 60 -> 60 ...
```

Komponenten kan resettes etter en vellykket sesjon og testes uten `sleep()`.

Dette er viktig: en unit-test skal ikke måtte vente i 122 sekunder for å bevise at backoff fungerer.

Hovedløkken sover dessuten i korte intervaller slik at et termineringssignal kan stoppe klienten raskt selv mens den venter på reconnect.

Målet er å unngå reconnect-storm samtidig som shutdown forblir responsiv.
