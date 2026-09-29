# Lab: a small Sopel plugin

The goal is to demonstrate plugin architecture without building a complicated bot.

Create a simple `!hello` command that returns a short static response.

It requires no shell command, database, external API, operator status or secret, making it a good first plugin exercise.

Conceptually:

```text
IRC PRIVMSG
    |
Sopel parser/dispatch
    |
hello plugin
    |
reply through Sopel
    |
IRC PRIVMSG
```

Use the plugin API and syntax documented for the Sopel version actually installed.

Test that the bot starts with the plugin, `!hello` responds correctly, ordinary channel text is ignored, unknown commands do not crash the plugin, and the function still works after a reconnect.

The bot does not need channel operator status for this task. Permissions follow function, not the label “bot”.
