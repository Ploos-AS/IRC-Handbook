# Accounts and IRC services

On IRC, a **nick** and an **account** are different concepts.

A nick is the visible name used by an active IRC connection. An account is an identity that an IRC network can authenticate. You may therefore be logged into an account while using a different active nick.

Many traditional networks expose account and channel functions through **services**, commonly including NickServ and ChanServ. Exact commands vary between networks, so users should follow the documentation of the network they actually use.

Historically, users often identified to NickServ after connecting. Modern clients should generally use **SASL** when the network supports it, allowing authentication to happen during connection setup.

Accounts are normally network-specific. An account on one IRC network is not automatically a global identity on another network.
