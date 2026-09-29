# Single-pass tag-unescaping

IRCv3 message tags har egne escape-sekvenser.

En kjede med flere `replace()`-kall er risikabel fordi resultatet fra én erstatning kan bli input til neste. Da kan en sekvens i verste fall dekodes mer enn én gang.

Eksempelparseren går derfor gjennom tag-verdien én gang, tegn for tegn. En backslash introduserer høyst én escape-operasjon.

Dette gir mer forutsigbar parsing av både kjente og ukjente escape-koder.
