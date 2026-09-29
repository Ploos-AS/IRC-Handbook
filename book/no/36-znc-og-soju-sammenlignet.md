# ZNC og soju sammenlignet

ZNC og soju løser overlappende problemer, men de har ulik historie og design.

| Tema | ZNC | soju |
|---|---|---|
| Grunnrolle | IRC-bouncer | IRC-bouncer |
| Historisk modell | etablert klassisk/modulær bouncer | moderne IRCv3-orientert bouncer |
| Utvidelser | omfattende modulkonsept | mer fokus på protokoll og bouncer-state |
| Flere nettverk | ja | ja |
| Flere klienter | støttes, opplevelsen avhenger av klient/protokoll | sentralt moderne brukstilfelle |
| Historikk | buffer/playback-funksjoner | moderne historikk/state-modell |
| IRCv3 | støtte avhenger av funksjon og versjon | sentralt i designet |

Tabellen er en arkitektursammenligning, ikke en rangering.

## Når du vurderer en bouncer

Undersøk det konkrete miljøet:

- hvilke klienter skal brukes?
- trenger du flere samtidige enheter?
- hvilke IRCv3-funksjoner trenger klientene og nettverkene?
- hvor mye historikk ønsker du å lagre?
- hvordan skal brukere administreres?
- hvordan tas backup?
- hvordan oppgraderes tjenesten?
- ønsker du moduler/utvidelser?

Deretter tester du kravene mot den faktiske versjonen du planlegger å drifte.

## Viktigste lærdom

Bounceren er infrastruktur. Velg og drift den ut fra ønsket arkitektur, sikkerhet og klientopplevelse, ikke bare navnet på programmet.
