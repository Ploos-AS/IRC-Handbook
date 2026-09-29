# Server rules instead of hard-coding

Several ISUPPORT values can now drive real client behaviour: PREFIX describes membership status, CHANMODES describes mode parameter classes, CASEMAPPING controls identifier comparison, CHANTYPES identifies channel prefixes and NICKLEN describes a nickname limit.

The broader design rule is simple: learn the rules advertised by the server instead of pretending every IRC network behaves identically.

The next step is to use these building blocks to parse MODE messages and maintain channel state.
