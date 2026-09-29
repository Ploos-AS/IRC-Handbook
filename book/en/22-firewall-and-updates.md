# Firewall and updates

An IRC shell normally needs very few inbound services.

At first, SSH is the primary inbound service. The IRC client itself makes outbound connections to IRC networks, so there is no reason to expose arbitrary inbound IRC ports merely because the machine is used for IRC.

A bouncer will later need its own inbound listener; we expose that only when the bouncer is actually installed.

Use one clearly managed firewall approach and document the policy. A provider network firewall can add another layer, but does not replace understanding which services are listening on the host.

Apply security updates regularly. Automated security updates can be useful, but the server still needs monitoring and a plan for required reboots.

Before major upgrades, have a working backup, know the recovery path, check disk space and read relevant release notes. An IRC shell should be boring to operate; stability is a feature.
