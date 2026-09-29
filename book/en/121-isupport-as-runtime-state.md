# ISUPPORT as runtime state

Numeric 005, RPL_ISUPPORT, describes properties of the IRC server. Parsing the line is not enough if the rest of the client continues to use hard-coded assumptions.

The example now has `ServerFeatures`. Every 005 message updates the same state for the lifetime of the connection, turning advertised server rules into data the client can actually use.
