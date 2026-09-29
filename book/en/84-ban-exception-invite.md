# Ban, exception and invite lists

Classic list modes often include b, e and I, depending on the server's CHANMODES advertisement.

For example, `MODE #retro +b *!*@bad.example` adds an entry and the corresponding -b removes one. Mask semantics and server-specific extensions are separate topics; the important parser lesson is that list modes consume parameters and their mode letters should be learned from ISUPPORT.
