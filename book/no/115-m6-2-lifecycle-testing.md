# M6.2: lifecycle-testing

Hardening må testes på de situasjonene som opprinnelig var vanskelige.

Unit-testene bruker `socketpair()` for å kontrollere at en stille peer kan avbrytes og at fragmenterte IRC-linjer fortsatt settes sammen riktig.

Fake-server-integrasjonstesten holder forbindelsen stille etter CAP-forhandling. Testen setter så stop-flagget og forventer `QUIT :Shutting down`.

Dermed tester vi ikke bare funksjonen som setter flagget; vi tester at hele receive-livssyklusen faktisk reagerer på det.
