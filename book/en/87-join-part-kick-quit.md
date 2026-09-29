# JOIN, PART, KICK and QUIT

JOIN adds the sender to the relevant channel, PART removes the sender, and KICK removes the nickname named by the event.

QUIT is broader: the user leaves the IRC connection and must be removed from every known channel. Our small example models one channel, but the same event rule applies when a larger client owns many ChannelState objects.
