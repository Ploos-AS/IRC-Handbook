# NICK changes and identity

A nickname can change while a user remains in a channel. If Bob has voice and changes nickname to Robert, that membership status must survive the rename.

`ChannelState.rename_member()` therefore moves the member to a new CASEMAPPING-normalized key while preserving its mode set. This also demonstrates why a nickname should not be treated as a permanent identity.
