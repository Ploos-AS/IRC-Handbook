# 153. NAMES as a snapshot

A NAMES list is not live state. It is a snapshot delivered through one or more `353` messages and completed by `366`.

This matters when normal IRC events arrive while the snapshot is being transferred. A user may appear in an old `353`, send `PART`, and then appear again in a later piece of the snapshot.

The example bot therefore builds NAMES in separate pending state. Live events are journaled while NAMES is active. At `366`, the snapshot is installed atomically and the journal is replayed in the same order in which the events arrived.

Older snapshot data can therefore not override newer live data.
