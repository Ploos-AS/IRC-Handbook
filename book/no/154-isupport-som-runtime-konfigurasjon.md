# 154. ISUPPORT som runtime-konfigurasjon

Numerisk `005` beskriver egenskaper ved serveren vi faktisk er koblet til. Verdier som `CASEMAPPING`, `PREFIX`, `CHANMODES` og `CHANTYPES` bør derfor behandles som runtime-konfigurasjon, ikke hardkodes som universelle IRC-regler.

M6.11 re-keyer eksisterende medlemsstate dersom CASEMAPPING endres. Status-modes beholdes, og kollisjoner mellom nøkler slås sammen.

`CHANTYPES` brukes også når MODE skal routes til en kanal. En server som annonserer andre kanalprefikser enn standardverdiene kan dermed modelleres uten en hardkodet liste i klienten.
