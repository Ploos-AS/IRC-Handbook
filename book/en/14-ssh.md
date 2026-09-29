# SSH

SSH is the normal way to access a modern shell server securely.

```sh
ssh user@shell.example.net
```

The client uses the server's host key to help detect unexpected changes in server identity. Do not develop the habit of blindly accepting security warnings.

Key-based authentication is generally preferable to repeatedly entering an account password. A modern key pair can, for example, be created with:

```sh
ssh-keygen -t ed25519
```

The private key stays on the client machine. The public key may be installed in the server account, normally through `~/.ssh/authorized_keys`.

Never share the private key.

A shared shell is also not automatically an appropriate place for sensitive secrets. Its administrator controls the host. Later we build our own server where more of the security policy is under our control.
