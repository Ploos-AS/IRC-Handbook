# M6.2: lifecycle testing

Hardening should test the situations that were difficult in the first place.

Unit tests use `socketpair()` to verify that a silent peer can be interrupted while fragmented IRC lines are still assembled correctly. The fake-server integration test remains silent after CAP negotiation, then expects `QUIT :Shutting down` after the stop flag is requested.

This tests the complete receive lifecycle rather than merely the flag setter.
