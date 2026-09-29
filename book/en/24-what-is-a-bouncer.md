# What is an IRC bouncer?

An IRC bouncer, often abbreviated **BNC**, sits between your IRC client and the IRC network.

```text
Client -> Bouncer -> IRC server
```

From the client's perspective the bouncer behaves like an IRC server, while toward the network it behaves like an IRC client.

Its central feature is that the upstream IRC connection can remain active while local clients disconnect. Depending on the implementation, bouncers can also provide multiple networks, several client devices, centralized configuration and message history/playback.

A shell and a bouncer are different architectures. With a shell you remotely operate a client running on the server. With a bouncer your IRC client can remain local and connect through the bouncer.
