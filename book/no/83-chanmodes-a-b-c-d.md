# CHANMODES A, B, C og D

`CHANMODES` beskriver parameterreglene for channel modes.

For eksempel:

```text
CHANMODES=beI,k,l,imnst
```

kan forstås som fire klasser:

- A: list modes, som ban/exception/invite-lister; parameter ved endring
- B: modes som bruker parameter både ved setting og fjerning
- C: modes som bruker parameter når de settes
- D: enkle flaggmodes uten parameter

Dermed trenger `+l 50` en verdi, mens `-l` ikke gjør det. `+i` trenger ingen verdi.

Det er denne informasjonen parseren bruker når den kobler mode-tegn til de etterfølgende parameterne.
