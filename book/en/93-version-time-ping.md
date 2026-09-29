# VERSION, TIME and PING

VERSION, TIME and PING are classic CTCP queries. The example bot responds only when a query is sent directly to its nickname through PRIVMSG, and responses use NOTICE.

VERSION identifies only the educational program. PING echoes its opaque argument without interpreting it. TIME deliberately returns fixed text rather than the host's local clock, avoiding unnecessary time and timezone disclosure.
