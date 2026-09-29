# Test the bot without the Internet

Protocol code should be testable without connecting CI to a public IRC network.

Run the repository tests with:

```sh
cd examples/minimal-bot
python3 -m unittest -v
```

They cover CRLF encoding, line-injection rejection, PING/PONG, joining after numeric 001, channel and private `!hello`, ignored ordinary text and PRIVMSG parsing.

The key design choice is to make:

```text
IRC line -> zero or more response lines
```

a small deterministic function. Most protocol behaviour can therefore be tested quickly and reproducibly.

The next step is a local fake IRC server that exercises socket framing and a complete registration session without using a public network.
