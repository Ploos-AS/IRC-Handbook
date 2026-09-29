# M6.9: protocol cleanup

M6.9 handler om å redusere antall steder som kan være nesten riktige.

CAP har nå én state machine. SASL-mekanismeutvekslingen er separat. Tag-unescaping har eksplisitte regresjonstester, og response-helperen kan bare behandle CAP når den får en ekte `Negotiation`-instans.

Dette er mindre spektakulært enn nye features, men viktig: protokollkode blir tryggere når samme regel ikke finnes i flere varianter.

Neste steg bør være å kjøre og kvalifisere hele testmatrisen i CI og deretter begynne å splitte den voksende eksempelklienten i små moduler uten å miste den pedagogiske lesbarheten.
