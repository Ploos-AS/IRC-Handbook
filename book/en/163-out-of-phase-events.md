# Out-of-phase events

Network programs must tolerate more than the expected happy path. Messages can be delayed, duplicated, or arrive after the client has already advanced to another phase. We therefore test not only what Registration should do with expected messages, but also what it must **not** do.

An important example is a late CAP ACK after 001 has already registered the client. It must not reopen CAP negotiation and must never cause another JOIN. Likewise, a 903 without active SASL is inert; it must not pretend that authentication has just completed.

This gives us a useful invariant:

> An event that is invalid in the current phase must not move the state machine backwards or repeat an already completed side effect.

JOIN is one such side effect. M6.13 allows the welcome to trigger it once, while later or duplicated registration events cannot produce an additional JOIN.

When we later build more advanced reconnect and membership policy, this distinction is essential: the registration machine decides when registration is complete; the membership system decides what we want to do afterwards.