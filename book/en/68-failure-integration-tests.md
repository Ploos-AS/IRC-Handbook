# Integration tests for failure paths

The fake server now exercises more than the happy path: ordinary registration, numeric 433 nickname collision, server ERROR, required SASL with the capability missing, and required SASL with authentication failure.

Network software is only robust when unwanted but valid protocol paths are specified and tested too.

All scenarios still use loopback sockets and synthetic credentials only.
