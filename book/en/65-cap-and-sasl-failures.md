# CAP and SASL failure paths

A state machine must define failure paths as well as success paths.

The minimal bot now handles CAP LS without SASL, CAP NAK and SASL failure numerics 904 through 907. The educational client ends capability negotiation cleanly with `CAP END` rather than becoming stuck.

That is a teaching policy, not a universal production policy. A strict deployment may instead require SASL and disconnect when authentication fails. Protocol mechanism and deployment policy are separate concerns.
