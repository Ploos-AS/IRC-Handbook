# M6.9: protocol cleanup

M6.9 reduces the number of places that can be almost correct.

CAP now has one state machine, SASL mechanism exchange remains separate, tag unescaping has explicit regression tests, and the response helper handles CAP only when given a real `Negotiation` instance.

This is less visible than adding features, but protocol code becomes safer when the same rule does not exist in multiple variants.

The next step should qualify the complete test matrix in CI and then begin splitting the growing educational client into small modules without losing readability.
