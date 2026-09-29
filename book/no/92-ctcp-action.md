# CTCP ACTION og /me

Når en bruker skriver:

```text
/me vinker
```

sender klienten vanligvis en CTCP ACTION:

```text
PRIVMSG #retro :\x01ACTION vinker\x01
```

Mottakerklienten presenterer dette som en handling i stedet for vanlig melding.

ACTION er derfor ikke en forespørsel boten skal svare på. Eksempelboten parser den, men produserer ingen automatisk reply.

Det er et godt eksempel på skillet mellom å *forstå* en protokollmelding og å *reagere* på den.
