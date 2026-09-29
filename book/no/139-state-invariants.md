# State invariants

En state engine bør kunne kontrollere sine egne grunnregler.

`assert_registry_invariants()` verifiserer blant annet at kanalnøkkelen stemmer med aktiv CASEMAPPING, at medlemsnøkler stemmer med medlemmenes nick, og at medlemsstatus bare inneholder kjente PREFIX-modes.

Replay kan kjøre disse kontrollene etter hvert event. Da oppdages korrupsjon nær meldingen som introduserte den, ikke først hundre events senere.
