# SSH hardening without locking yourself out

Treat SSH changes carefully because SSH is the administrative entry point to the server.

First establish and verify key-based login, for example using an Ed25519 key created with:

```sh
ssh-keygen -t ed25519
```

Test a new, separate SSH connection before tightening authentication policy, and keep the existing administrative session open while testing.

Once key login is verified, typical goals include avoiding direct root login, reducing or disabling password authentication where appropriate, limiting access to required users, and keeping OpenSSH updated.

Exact directives depend on the installed OpenSSH version and hosting environment. Validate configuration before reloading the service.

Before hardening, also learn how to reach the provider's recovery or console facility. A configuration that permanently locks out its administrator is not a sound operational design.
