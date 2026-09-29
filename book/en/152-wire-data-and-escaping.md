# 152. Wire data and escaping

IRC contains control characters and escaping at several layers. It is easy to confuse the text `\\x01` with the actual CTCP delimiter byte 0x01, or the text `\\r\\n` with real CRLF.

The M6.10 tests therefore construct critical wire characters explicitly. This makes the distinction between Python source code and data on the IRC connection visible.

The same rule applies to IRCv3 message tags: unescaping must be a single pass. The output of one escape must not be interpreted again as the start of another escape.
