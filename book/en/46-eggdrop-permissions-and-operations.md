# Eggdrop: permissions and operations

A channel bot can gain significant power if granted operator status. Begin as a normal channel member and add privileges only when a documented function requires them.

Keep the identity layers separate:

```text
Unix service identity
        |
Eggdrop internal auth/state
        |
IRC bot account
        |
channel privileges
```

In a historical shell environment Eggdrop may run as a long-lived user process. On a server you control, a service manager can make startup, restart policy and process identity explicit.

Avoid aggressive restart loops. A broken configuration should not create thousands of rapid restart attempts.

Back up required configuration and state while handling secrets deliberately, and test restoration rather than assuming the backup is usable.
