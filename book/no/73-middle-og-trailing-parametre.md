# Middle og trailing parameters

IRC skiller mellom parametre som ikke inneholder mellomrom og et siste trailing-parameter som kan gjøre det.

```text
COMMAND one two :three four
```

blir:

```text
["one", "two", "three four"]
```

Kolonet er syntaks som markerer starten på trailing-parameteret; det er ikke en del av verdien.

Dette forklarer blant annet hvorfor:

```text
PRIVMSG #retro :Hei alle sammen
```

kan ha en melding med mellomrom.

Å forstå dette er viktigere enn å splitte IRC-linjer blindt på spaces.
