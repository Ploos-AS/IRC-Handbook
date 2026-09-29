# Channel modes og CHANMODES

Channel modes styrer kanaltilstand og kan ha forskjellige parameterregler.

ISUPPORT-tokenet `CHANMODES` deler modes i fire grupper:

```text
CHANMODES=A,B,C,D
```

Et vanlig eksempel kan ligne:

```text
CHANMODES=beI,k,l,imnst
```

Gruppene beskriver blant annet modes som alltid tar parameter, modes som tar parameter når de settes, og enkle flaggmodes.

Det viktige for klientdesign er at parameterbehovet ikke bør hardkodes fra én bestemt serverimplementasjon.

Minimal-klienten har derfor `parse_chanmodes()` som første byggestein for en senere MODE-parser.
