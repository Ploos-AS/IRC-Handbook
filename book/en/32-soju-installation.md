# soju: a modern IRC bouncer

soju is an IRC bouncer designed with modern IRC and IRCv3 usage in mind.

```text
IRC clients -> soju -> IRC networks
```

Run it as an unprivileged service identity rather than root. Treat configuration, state and any database as operational data that must be protected, backed up and considered during upgrades.

Package names, versions, database choices and service integration vary by platform and release. Follow the documentation for the version you actually deploy, and test in a controlled environment before exposing a listener to the Internet.
