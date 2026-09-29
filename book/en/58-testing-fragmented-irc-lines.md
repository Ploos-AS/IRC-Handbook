# Testing fragmented IRC lines

One of the most important integration tests concerns TCP rather than an IRC command.

The fake server deliberately splits some IRC lines across multiple writes. The bot must still reconstruct one complete protocol line.

This proves that the client does not make the classic mistake:

```text
one recv() == one protocol message
```

Instead it implements:

```text
TCP bytes -> buffer -> find LF -> complete IRC line -> parser
```

The same framing principle applies to many other stream-based network protocols.
