# State snapshots

Mutable runtime state is convenient internally but poor as a test interface.

`channel_snapshot()` and `registry_snapshot()` produce deterministic structures with sorted members, modes and lists. A snapshot shares no mutable sets with the live model, so later events cannot rewrite test history.
