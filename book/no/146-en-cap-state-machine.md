# Én CAP state machine

Protokollstate bør ha én autoritativ eier.

Tidligere kunne både `Negotiation` og `actions_for_message()` tolke CAP-meldinger. Det ga to implementasjoner av samme state machine, med risiko for at testhelperen og den virkelige session-løkken oppførte seg forskjellig.

CAP håndteres nå bare av `Negotiation`.
