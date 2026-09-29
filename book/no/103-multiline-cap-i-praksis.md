# Multiline CAP i praksis

Når serveren sender:

```text
CAP nick LS * :server-time account-tag
CAP nick LS :sasl=PLAIN message-tags
```

må klienten vente.

Etter første linje vet den ennå ikke hele capability-settet. Først når continuation-markøren `*` forsvinner, velger `Negotiation` hvilke capabilities som skal forespørres.

Dette hindrer at klienten starter forhandling for tidlig og overser capabilities som annonseres i senere fragmenter.
