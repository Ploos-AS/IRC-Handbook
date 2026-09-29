# soju: users, networks and security

Keep the identity layers separate:

```text
person
  |
  +-- soju user
         |
         +-- IRC network A -> IRC account A
         +-- IRC network B -> IRC account B
```

The client authenticates to the bouncer, while each upstream network can have its own IRC account and SASL configuration.

Protect Internet-facing downstream connections with TLS and certificate validation. Use TLS upstream where available and SASL where supported and appropriate.

Keep credentials out of Git and protect configuration and state with suitable Unix permissions. Multiple networks behind one bouncer remain independent IRC environments with their own accounts, channels and policies.
