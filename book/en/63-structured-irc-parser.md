# A structured IRC parser

The minimal bot now parses each line into a general message model containing tags, prefix, command and parameters.

This separates transport/protocol parsing from application behaviour. Features such as PRIVMSG handling no longer need to invent their own raw-string parsing rules.
