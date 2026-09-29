# VERSION, TIME og PING

Tre klassiske CTCP-queries er VERSION, TIME og PING.

Eksempelboten svarer bare når queryen sendes direkte til botens nick via `PRIVMSG`. Svar sendes som `NOTICE`.

VERSION identifiserer bare programmet som en pedagogisk IRC Handbook-bot. PING returnerer det mottatte argumentet uten å tolke det.

TIME demonstrerer en personvernbevisst policy: eksempelboten returnerer en fast tekst i stedet for lokal tid. Dermed lekker den ikke unødvendig klokke- eller tidssoneinformasjon.
