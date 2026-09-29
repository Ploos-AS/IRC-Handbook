# Users, resources and backup

A private one-person IRC shell is much simpler than a multi-user shell service.

Give different people separate Unix accounts rather than sharing one account and SSH key. This provides clear ownership and allows access to be revoked per user.

Misconfigured clients and bots can consume CPU, memory, process slots or disk space. Resource limits and monitoring therefore become important when operating a shared service.

Useful backup targets commonly include client and bouncer configuration, your own scripts, deliberately retained logs and documentation of the server setup. Private keys and other secrets require special handling and should not be copied casually into ordinary backups or Git repositories.

Test restoration. A backup that has never been restored is an assumption rather than demonstrated recovery.

This foundation later grows into:

```text
Debian
  +-- shell users
  +-- terminal clients
  +-- bouncers
  +-- bots
  +-- monitoring
  +-- backup
```

At that point we are moving from a personal IRC shell toward a real IRC hosting platform.
