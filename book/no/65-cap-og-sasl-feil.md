# CAP og SASL når ting går galt

En state machine må også definere feilveiene.

Minimalboten håndterer nå blant annet:

- CAP LS uten `sasl`
- CAP NAK
- SASL failure-numerics 904–907

I undervisningseksemplet avsluttes CAP-forhandlingen kontrollert med `CAP END` slik at forbindelsen ikke blir hengende i capability negotiation.

Dette betyr ikke at alle produksjonsklienter bør fortsette uten autentisering. En streng klient kan i stedet ha policyen:

```text
SASL required + SASL failed -> disconnect
```

Policy og protokollmekanikk er to forskjellige lag, og senere kan vi gjøre dette konfigurerbart.
