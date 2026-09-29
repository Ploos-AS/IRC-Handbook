# Skillet mellom CAP og SASL

CAP-forhandling og SASL-datautveksling henger sammen, men er ikke samme lag.

`Negotiation` bestemmer hvilke capabilities som forespørres og når SASL skal startes. Den vanlige meldingshandleren håndterer deretter `AUTHENTICATE +` og SASL-resultatnumerics.

Dette gjør ansvaret tydelig: capability-state ett sted, mekanismeutveksling et annet.
