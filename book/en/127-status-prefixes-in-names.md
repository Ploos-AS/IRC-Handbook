# Status prefixes in NAMES

A NAMES entry may look like @Alice, +Bob, %+Helper or Plain. These prefixes must not be hard-coded to only @ and +.

ISUPPORT PREFIX tells the client which visible prefix characters correspond to membership modes. The example can therefore parse multiple simultaneous statuses on one member and retain them as mode state.
