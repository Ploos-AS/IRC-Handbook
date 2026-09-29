# Lab: soju with multiple clients

The goal is to demonstrate the difference between merely preserving an upstream connection and actually using a persistent environment from multiple clients.

Connect client A to soju and verify bouncer authentication, upstream connectivity, identity, channels and messaging. Then connect a second client instance to the same soju user.

Disconnect A while B remains active. Exchange test traffic in an appropriate controlled environment, reconnect A, and inspect how state and history are presented. Repeat in the opposite direction.

Then add a second IRC network. Observe that one soju user can provide access to multiple networks without turning their separate IRC accounts into one global identity.

The resulting model is:

```text
multiple clients
      |
persistent bouncer state
      |
multiple independent IRC networks
```
