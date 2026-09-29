# Toward a persistent IRC identity

We can now separate three concepts: the active **connection**, the visible **nick**, and the authenticated **account**.

This makes the role of a bouncer much easier to understand.

Without one:

```text
Laptop ----> IRC network
```

With one:

```text
Laptop ----+
           |
Phone -----+--> Bouncer ----> IRC network
           |
Tablet ----+
```

The bouncer can maintain the IRC-side connection while individual clients come and go. Authentication can also happen at multiple boundaries: a client authenticates to the bouncer, and the bouncer can authenticate to the IRC network.

The classic shell approach is related but different:

```text
Laptop -> SSH -> shell server -> IRC client -> IRC network
```

Using `screen` or `tmux`, users could leave a terminal IRC client running after disconnecting their local terminal. Later chapters build both the classic shell model and modern bouncer model so their different roles become clear.
