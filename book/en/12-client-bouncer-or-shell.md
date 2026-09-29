# Client, bouncer or shell?

Three architectures are worth separating.

A local client:

```text
PC -> IRC client -> IRC network
```

A remotely running client on a shell:

```text
PC -> SSH -> tmux -> IRC client -> IRC network
```

And a local client using a bouncer:

```text
PC -> IRC client -> bouncer -> IRC network
```

With several devices the bouncer model becomes particularly useful:

```text
Desktop ---+
Laptop ----+--> bouncer --> IRC network
Phone -----+
```

Modern bouncers can provide more than a persistent connection, including history and multi-client functionality. The book builds these models practically so the reader can choose an architecture based on actual needs rather than treating one approach as universally correct.
