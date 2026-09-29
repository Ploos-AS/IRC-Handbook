# From plugin to our own bot

A plugin framework provides many facilities: IRC connectivity, parsing, event dispatch, reconnect logic, configuration, logging and often modern protocol support.

A custom client must take responsibility for more of those layers.

```text
plugin -> Sopel -> IRC
```

versus:

```text
function -> our parser/state -> TLS/socket -> IRC
```

A plugin is often the practical choice when the goal is to add IRC functionality on top of a maintained framework. A custom client is valuable for learning because it exposes how IRC actually works.

Our next bot will start small: establish TLS, register, read IRC lines, answer `PING`, join a channel, parse `PRIVMSG`, respond to one explicit command and reconnect with controlled retry.

Once that works, the mechanics underneath Eggdrop, EnergyMech, Dancer and Sopel become much easier to understand.
