# M6.8: transcript and property testing

M6.8 gives the state engine a permanent regression corpus and a small fuzz layer.

A failure found on a real network can now be reduced to a few IRC lines and committed to the corpus, turning the bug into permanent regression data.

This is an important protocol-engineering habit: bugs are not only fixed in code; they are preserved as tests.

The next natural step is to address technical debt now made easier to expose, especially duplicated CAP/SASL logic and stricter parser boundaries.
