# Accumulating multiple 005 lines

ISUPPORT does not necessarily fit in one message. A server may distribute tokens across several 005 replies.

`ServerFeatures.update()` merges new tokens into existing state. A token prefixed with a minus removes a previously advertised value, after which the educational client uses a conservative defined fallback where appropriate.
