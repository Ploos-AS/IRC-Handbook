# ZNC: TLS and login

A client connection to ZNC introduces a separate security boundary:

```text
IRC client -> TLS + ZNC authentication -> ZNC -> upstream IRC
```

Keep the two authentication contexts distinct:

```text
client -> ZNC:        ZNC_USER + ZNC_PASSWORD
ZNC -> IRC network:  IRC_ACCOUNT + IRC_SECRET
```

They do not need to use the same credentials.

An Internet-accessible ZNC listener should use TLS with certificate validation. Open only the firewall port actually selected for the TLS listener and document that choice rather than assuming every deployment uses the same port.

Troubleshoot layer by layer: listener, TCP reachability, TLS, ZNC authentication, then upstream IRC connectivity.
