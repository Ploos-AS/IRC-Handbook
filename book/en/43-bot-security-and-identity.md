# Bot security and identity

A bot receives network input and reacts automatically, making security boundaries important.

Use a separate IRC account for the bot where the network supports accounts:

```text
human account != bot account
```

On a server, avoid running bots as root. Separate Unix identities can also isolate different services where appropriate.

Keep IRC passwords, SASL secrets, tokens and private keys out of Git. Protect secret-bearing configuration with appropriate file permissions and backup handling.

Treat IRC messages as untrusted input. A command argument must remain data rather than being blindly interpolated into a shell command.

Apply least privilege to channel modes, files, network access and external API permissions. A bot should receive only the access required for its actual job.
