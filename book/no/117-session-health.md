# Session health

En TCP-tilkobling er ikke nødvendigvis en frisk IRC-sesjon.

I eksemplet regnes forbindelsen først som etablert når serveren sender numeric `001`, welcome. Da har registreringsfasen lykkes.

```text
TCP connect ≠ healthy IRC session
001         = registrert session
```

Dette gir reconnect-policyen et enkelt, observerbart health-signal.
