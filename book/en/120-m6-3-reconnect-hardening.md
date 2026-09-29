# M6.3: reconnect hardening

Reconnect is a state machine, not merely a while-true loop.

M6.3 adds explicit EOF/disconnect, explicit local shutdown, health only after numeric 001, backoff reset only after a healthy session, and separation of permanent authentication-policy failures from reconnectable failures.

The next hardening step should wire 005 server features into live runtime state so CASEMAPPING, PREFIX and CHANMODES actively control behavior rather than existing only as parser helpers.
