# Parser contracts

A robust parser does not need to accept everything. It needs predictable boundaries.

Invalid structure should either produce a controlled `ValueError` or be ignored by an explicit higher layer. The parser should not silently repair ambiguous protocol input.

The transcript fuzzing introduced in M6.8 makes these contracts particularly useful.
