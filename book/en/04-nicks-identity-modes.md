# Nicks, identity and modes

A nick is the most visible part of your IRC identity, but it is not the whole identity.

You can normally change it with:

```text
/nick NewNick
```

Modern networks often provide accounts and services that make identity more persistent. We cover those later with SASL and NickServ.

The `/whois Nick` command asks for information about a user. What is returned depends on the network and its privacy rules.

IRC uses **modes** for many user and channel settings. Channel members may also carry status modes. A familiar example is channel operator status, often displayed as `@`.

A channel operator is not the same thing as an IRC operator (IRCop). The former has privileges in a channel; the latter performs administrative duties for the IRC network.

At protocol level a mode change may look like:

```text
MODE #retro +o Ada
```

Throughout this book we first learn the user-facing feature and then examine how IRC represents it on the wire.
