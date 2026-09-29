# CHANMODES A, B, C and D

CHANMODES describes channel-mode parameter rules. A value such as `beI,k,l,imnst` divides modes into four classes: list modes, modes with parameters on set and unset, modes with parameters only when set, and simple flag modes.

This is why `+l 50` consumes a value while `-l` does not, and why `+i` needs no value. The parser uses these advertised classes when associating mode letters with parameters.
