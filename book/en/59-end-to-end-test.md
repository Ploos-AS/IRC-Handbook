# End-to-end test of the minimal bot

Run the complete suite with:

```sh
cd examples/minimal-bot
./run_tests.sh
```

or `python3 -m unittest -v`.

The suite now has two layers: deterministic unit tests for line-to-response behaviour and a local integration test that starts a real loopback TCP listener and runs the normal `run_session()` code against it.

The fake server records the bot's actual transcript and checks the expected NICK, USER, JOIN, PONG and PRIVMSG sequence.

This exercises the real path:

```text
socket -> recv -> framing -> parser/state -> response -> send
```

The next step is to run these tests in CI and then extend the client with IRCv3 CAP and SASL while preserving the deterministic test model.
