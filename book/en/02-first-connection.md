# Your first IRC connection

To use IRC you initially need only three things: an IRC network, a client, and a nick.

## Choose a client

IRC clients include graphical desktop applications, terminal programs, mobile apps, and web clients. We compare them later. At this stage, understanding the model matters more than finding the perfect client.

A client normally needs a server address, port, TLS setting, desired nick, and optionally an account and SASL password. Use TLS when the network provides it.

## Connecting

The client opens a connection to a server and registers your identity. The server sends welcome messages plus information about the network and supported features.

You can then join a channel:

```text
/join #channel
```

Type ordinary text in the channel window to talk to its participants.

## Essential commands

```text
/join #channel
/part #channel
/nick NewNick
/msg Nick Hello!
/whois Nick
/me is testing IRC
/quit
```

Lines beginning with `/` are normally interpreted by the client as commands. Ordinary text becomes a message to the active conversation.

## Channels and private conversations

A channel is a shared conversation space. A private message is addressed directly to a nick:

```text
/msg Ada Hello!
```

Many clients then open a separate conversation window.

## One important habit

Do not mistake the IRC window for IRC itself. The client is only the user interface. Underneath it is a text protocol between client and server. Later we will inspect those messages directly and write a minimal client/bot ourselves.
