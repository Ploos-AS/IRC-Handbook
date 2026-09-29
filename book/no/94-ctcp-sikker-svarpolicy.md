# En trygg CTCP-svarpolicy

Automatiske svar bør være konservative.

Eksempelboten:

- svarer ikke på CTCP sendt til en kanal
- svarer aldri automatisk på CTCP i `NOTICE`
- svarer ikke på `ACTION`
- ignorerer ukjente CTCP-kommandoer
- bruker `NOTICE` for støttede svar
- avslører ikke lokal klokke i TIME

Dette reduserer risikoen for svarsløkker og gjør boten mindre egnet som reflektor for uønsket trafikk.

En full klient kan støtte mer CTCP, men «jeg kan parse dette» betyr ikke automatisk «jeg bør svare på dette».
