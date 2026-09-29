# M6.8: transcript- og property-testing

M6.8 gir state engine et permanent regresjonscorpus og et enkelt fuzz-lag.

Vi kan nå ta en feil funnet på et virkelig nettverk, redusere den til noen IRC-linjer og legge sekvensen i corpus. Fra da av blir den en varig regresjonstest.

Dette er en viktig arbeidsmetode for protokollprogramvare: bugs blir ikke bare fikset i kode; de blir bevart som testdata.

Neste naturlige steg er å rydde den tekniske gjelden vi nå kan se tydeligere, særlig duplisert CAP/SASL-logikk og strengere parsergrenser.
