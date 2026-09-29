# Preface

IRC is one of the Internet's oldest communication protocols still in active use. It is simple enough that you can understand the protocol traffic directly, yet flexible enough to support large networks, persistent identities, bouncers, bots and self-hosted infrastructure.

This book is for readers who want to understand IRC in practice. We begin with the first connection and gradually build toward a complete persistent IRC environment.

No prior Unix, shell-account, bot or server-administration experience is required.

## What you will learn

By the end of the book, you should be able to:

- connect to an IRC network and use the essential commands
- understand channels, nicks, accounts and modes
- use TLS and SASL
- use terminal clients such as Irssi and WeeChat
- understand and use shell accounts
- keep IRC sessions running through SSH, tmux or screen
- configure and use an IRC bouncer
- understand the differences between ZNC, soju and classic bouncer approaches
- run and administer IRC bots
- write a small IRC bot yourself
- read basic IRC protocol traffic
- understand modern IRCv3 features
- operate a small IRC environment on a VPS or self-hosted server
- make sensible security and privacy choices

## The book's progression

We start with:

```text
Your computer -> IRC client -> IRC network
```

By the end, we build toward:

```text
Laptop ----+
Phone ------+--> Bouncer --> IRC network
Web --------+       |
                    +--> Bot
                    +--> More IRC networks
                    |
                 Shell/VPS
                    |
             SSH + tmux + tools
```

The goal is not merely to memorize commands. The goal is to understand how the IRC ecosystem fits together.
