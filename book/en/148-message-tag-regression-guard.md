# A regression guard for message tags

Tag unescaping was previously implemented as a chain of replace operations. That code is tempting but may decode text produced by an earlier replacement.

Tests now explicitly cover known escapes, unknown escapes, a backslash producing a sequence that must not be decoded again, and a trailing backslash.

Single-pass behavior is therefore a tested contract.
