# What is IRC?

Internet Relay Chat (IRC) is an open protocol for real-time text communication. Instead of one vendor owning the entire service, the IRC world consists of many independent networks. A network contains one or more IRC servers cooperating to provide users with a shared set of channels and conversations.

## The basic model

You run an **IRC client**. It connects to an **IRC server**, which belongs to an **IRC network**. On that network you can join **channels**, whose names commonly begin with `#`.

```text
IRC client -> IRC server -> IRC network -> #channel
```

A **nick** is the name by which other users see you. IRC also has username and host concepts, but these are not the same thing as your nick.

## IRC is a protocol, not a website

This distinction is fundamental. IRC is closer to email than to a single chat service: many client and server implementations can speak the same protocol. You can therefore change clients without changing networks, and networks can be operated independently.

## Why learn IRC today?

IRC remains useful because it is simple enough to understand while still supporting robust communication systems. You can use a desktop client, keep a client running on a shell account, connect several devices through a bouncer, or operate the entire infrastructure yourself.

This book starts with ordinary IRC use and progresses toward TLS and SASL, shell accounts and SSH, tmux and screen, ZNC and soju, bots, IRCv3, IRC servers, and a persistent IRC environment on a VPS.

The goal is not merely to *use* IRC. By the end of the book, you should understand what happens between client and server and be able to build your own setup.
