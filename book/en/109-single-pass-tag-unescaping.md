# Single-pass tag unescaping

IRCv3 message tags define escape sequences. A chain of replace operations is risky because output from one replacement can become input to another.

The example parser now walks a tag value once, character by character. A backslash introduces at most one escape operation, making known and unknown escape sequences more predictable.
