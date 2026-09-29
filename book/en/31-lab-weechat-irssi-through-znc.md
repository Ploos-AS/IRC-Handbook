# Lab: WeeChat and Irssi through ZNC

The goal is to demonstrate that the local IRC client can disappear while ZNC preserves the upstream session.

Configure WeeChat or Irssi to use ZNC as its server, using your deployment values:

```text
server: BOUNCER_HOST
port:   BOUNCER_TLS_PORT
user:   ZNC_LOGIN
secret: ZNC_SECRET
TLS:    enabled + certificate validation
```

Exact syntax varies by client and ZNC version.

First verify normal IRC operation. Then completely exit the local client while ZNC remains running. Reconnect later and verify that the upstream session was not dependent on the local client process.

With appropriate test participants, exchange test messages while the local client is absent and inspect how buffered history is presented after reconnection.

Finally switch from WeeChat to Irssi using the same ZNC account. This demonstrates the central architectural change: the IRC identity and upstream session are no longer tied to one local client program.

The next section repeats the exercise with soju and examines a more IRCv3-oriented multi-client model.
