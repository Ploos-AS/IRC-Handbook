# Snapshot diffs

When replay continues, it is useful to ask what actually changed.

`snapshot_diff(before, after)` reports channel keys that were added, removed or changed. A compact diff is often more educational than dumping the entire state after every event because it highlights the consequence of one protocol transition.
