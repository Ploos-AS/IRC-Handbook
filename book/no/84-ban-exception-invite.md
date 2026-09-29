# Ban, exception og invite-lister

Klassiske list modes inkluderer ofte `b`, `e` og `I`, avhengig av serverens CHANMODES.

Et eksempel:

```text
MODE #retro +b *!*@bad.example
```

legger et element til en liste. `-b` med samme parameter fjerner det.

Selve mask-formatet og hvilke utvidelser serveren støtter er et eget tema. På dette nivået er poenget at klienten først må forstå at list modes konsumerer parametre.

En robust klient lærer hvilke bokstaver som tilhører denne klassen fra ISUPPORT.
