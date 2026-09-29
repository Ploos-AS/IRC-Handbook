# Når SASL er et krav

Det er forskjell på å støtte SASL og å kreve SASL.

Minimalboten har nå policyflagget:

```text
IRC_SASL_REQUIRED=1
```

Når dette er aktivt avsluttes sesjonen dersom serveren ikke annonserer SASL, avviser capability-forespørselen eller autentiseringen feiler.

Dermed kan en deployment si eksplisitt: «ikke fortsett som uautentisert klient».

Policy ligger over protokollmekanikken. Den samme CAP/SASL-parseren kan derfor brukes både i en tolerant undervisningsmodus og en strengere driftsmodus.
