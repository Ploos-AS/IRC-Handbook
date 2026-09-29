# CAP LS continuation and capability values

A capability list may require more than one IRC message. A server can therefore send multiple CAP LS replies and use * to indicate continuation.

The example client's `CapabilityState` accumulates those fragments before publishing the completed list. Capabilities may also have values, such as `sasl=PLAIN,EXTERNAL`, so advertisements are stored as names with optional values rather than only a set.
