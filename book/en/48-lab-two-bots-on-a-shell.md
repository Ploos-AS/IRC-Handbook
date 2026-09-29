# Lab: two bots on the IRC shell

Run Eggdrop and EnergyMech as separate services in the same controlled lab environment:

```text
Debian VPS
  |
  +-- eggdrop-user -> Eggdrop ----+
  |                               |
  +-- mech-user ----> EnergyMech -+--> IRC test environment
```

Do not share Unix identities or credentials merely because the bots use the same host.

Verify process ownership and configuration permissions. Give the bots separate IRC identities and, where supported, separate IRC accounts. Join both to a controlled test channel without operator privileges and test a harmless function.

Then perform a controlled disconnect and observe detection, retry behaviour, reconnection and channel recovery. After validating configuration and backups, test a planned host reboot and verify that the chosen service model restores the bots without manual login.

Finally grant a specific channel privilege only where a lab function actually requires it. This demonstrates that operating a bot is more than simply making a program connect.
