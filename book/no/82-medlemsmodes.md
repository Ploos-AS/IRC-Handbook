# Medlemsmodes

Modes fra `PREFIX` gjelder medlemsstatus i en kanal.

Med:

```text
PREFIX=(ov)@+
```

betyr `+o alice` operatorstatus og `+v bob` voice.

Et nettverk som annonserer:

```text
PREFIX=(qaohv)~&@%+
```

har flere statusnivåer.

MODE-parseren får derfor PREFIX-modebokstavene som input. Alle slike medlemsmodes krever et nick-parameter både når status legges til og fjernes.
