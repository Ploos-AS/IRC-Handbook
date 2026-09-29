# Events during a snapshot

IRC is asynchronous. A JOIN can arrive while a multi-line 353 sequence is still in progress.

If snapshot completion blindly removes everything absent from 353, a brand-new JOIN can disappear. A JOIN received during an active NAMES generation is therefore added both to membership state and to the generation's observed set.

Snapshots and live events must cooperate.
