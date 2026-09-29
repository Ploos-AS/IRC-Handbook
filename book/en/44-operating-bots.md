# Operating IRC bots

A bot expected to remain available is a service, not merely a terminal program that happened to be started once.

The classic shell model is:

```text
SSH -> shell -> screen/tmux -> bot
```

On a server you administer, a controlled service-manager model can provide explicit process identity, restart policy and logging.

Monitor whether the process runs, whether it remains connected to the expected IRC network, whether reconnect works, whether logs or databases grow unexpectedly, whether integrations fail and whether credentials remain valid.

A robust bot must tolerate temporary DNS failure, broken TCP connections, IRC server restarts, disconnects and host reboots. Retry behaviour should use controlled backoff rather than an aggressive tight loop.

Log only what operations actually require. IRC message content may contain personal or private communication, so retention and backups should be deliberate choices.
