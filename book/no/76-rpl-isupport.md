# 005 RPL_ISUPPORT

`005 RPL_ISUPPORT` lar serveren beskrive egenskaper ved akkurat det IRC-nettverket klienten er koblet til.

Et eksempel kan se slik ut:

```text
:srv 005 nick CHANTYPES=#& PREFIX=(ov)@+ CASEMAPPING=rfc1459 NICKLEN=30 :are supported
```

Dette kan gi strukturerte egenskaper:

```text
CHANTYPES   -> #&
PREFIX      -> (ov)@+
CASEMAPPING -> rfc1459
NICKLEN     -> 30
```

Noen tokens er bare flagg. Et token prefikset med `-` kan angi at en tidligere annonsert egenskap fjernes.

Minimalboten har nå `parse_isupport()` for å demonstrere denne modellen.

Poenget er større enn helperen: robuste IRC-klienter bør lære serverens regler i stedet for å hardkode alle nettverk som om de var identiske.
