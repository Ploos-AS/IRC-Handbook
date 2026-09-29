# From MODE parser to channel state

The data path is now: 005 ISUPPORT → PREFIX and CHANMODES → MODE line → a list of ModeChange objects → channel state.

The educational parser deliberately stops at the change list. A separate state layer can later maintain channel flags, key and limit values, per-member status and list modes.

Keeping parsing and state separate makes both easier to test and allows protocol transcripts to be replayed to reconstruct channel state.
