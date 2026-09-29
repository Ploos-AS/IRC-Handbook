# Channel modes and CHANMODES

Channel modes represent channel state and have different parameter rules. The ISUPPORT `CHANMODES` token divides modes into four classes, for example `CHANMODES=beI,k,l,imnst`.

A client should learn these parameter rules from the server rather than hard-coding one server implementation. The minimal client now includes `parse_chanmodes()` as the first building block for a later MODE parser.
