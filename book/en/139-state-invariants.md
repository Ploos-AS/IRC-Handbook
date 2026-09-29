# State invariants

A state engine should be able to check its own fundamental rules.

`assert_registry_invariants()` verifies that channel keys match active CASEMAPPING, member keys match member nicks, and membership status contains only known PREFIX modes.

Replay can check these invariants after every event, locating corruption close to the transition that introduced it.
