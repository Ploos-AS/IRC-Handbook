# 154. ISUPPORT as runtime configuration

Numeric `005` describes properties of the server to which we are actually connected. Values such as `CASEMAPPING`, `PREFIX`, `CHANMODES` and `CHANTYPES` should therefore be treated as runtime configuration rather than hard-coded universal IRC rules.

M6.11 re-keys existing member state when CASEMAPPING changes. Status modes are preserved and key collisions are merged.

`CHANTYPES` is also used when routing MODE to a channel. A server advertising channel prefixes different from the defaults can therefore be modeled without a hard-coded list in the client.
