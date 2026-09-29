# Reconnect and backoff

Network connections disappear, so a bot must establish a new session without hammering the server with connection attempts.

The example uses a simple bounded exponential delay:

```text
2s -> 4s -> 8s -> 16s -> 32s -> 60s
```

After reconnect, registration starts again: TCP/TLS, NICK/USER, wait for registration, then JOIN. State from the old socket cannot simply be assumed valid.

A production client must handle additional cases such as nick collisions, server errors, rate limits, SASL, IRCv3 CAP, multiple channels, desired-state restoration and controlled shutdown. The minimal bot is a foundation, not the endpoint.
