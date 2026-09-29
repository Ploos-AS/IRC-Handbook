# Minimal IRC bot

Educational IRC bot used by the Ploos IRC Handbook.

It intentionally uses only the Python standard library so the protocol mechanics remain visible.

## Test

```sh
cd examples/minimal-bot
python3 -m unittest -v
```

## Configuration

Runtime configuration comes from environment variables:

- `IRC_HOST`
- `IRC_PORT` (default `6697`)
- `IRC_NICK`
- `IRC_CHANNEL`
- `IRC_TLS` (default enabled)

Do not commit real credentials.

The example deliberately starts without SASL. SASL and IRCv3 CAP negotiation are added in later handbook stages after the basic registration state machine is understood.
