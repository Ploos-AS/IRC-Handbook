# Networks, servers and channels

An IRC **network** is the logical service users connect to. It may consist of several servers exchanging information about users, channels and messages.

A **server** accepts client connections and participates in that network. This distinction matters: the server is the system your client is directly connected to, while the network is the larger IRC environment.

A **channel** is a shared conversation space, commonly named with a leading `#`:

```text
/join #retro
```

Channels also have state: membership, topics, modes, operator status and, depending on the network, invitation or ban lists and other features.

IRC networks are separate worlds. A nick or `#retro` channel on one network is not automatically related to the same name on another network. Later, a bouncer will let us manage persistent connections to several networks conveniently.
