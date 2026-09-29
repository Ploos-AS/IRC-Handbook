# CAP NEW, DEL and ACK

Capability state can change after registration. CAP NEW advertises newly available features, CAP DEL removes them, and CAP ACK confirms requested changes.

The minimal client therefore distinguishes available capabilities from enabled capabilities. Removing a capability also removes it from enabled state.
