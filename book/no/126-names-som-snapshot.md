# NAMES som kanal-snapshot

Når en klient joiner en kanal finnes det ofte allerede brukere der. JOIN-events alene kan derfor ikke bygge komplett medlemsstate.

Numeric 353, RPL_NAMREPLY, gir en liste over kanalens medlemmer. Eksempelklienten bruker disse svarene som bootstrap for `ChannelState`.

Numeric 366 markerer slutten på NAMES-sekvensen. Etter dette fortsetter vanlig event-replay å holde modellen oppdatert.
