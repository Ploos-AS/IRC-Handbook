# CASEMAPPING

IRC-navn kan ikke alltid sammenlignes med vanlig Unicode/Python `.lower()`.

Serveren kan annonsere:

```text
CASEMAPPING=ascii
CASEMAPPING=rfc1459
CASEMAPPING=strict-rfc1459
```

ASCII-mapping gjør i hovedsak bokstavsammenligning case-insensitive.

RFC1459-mapping behandler i tillegg enkelte ASCII-tegn som ekvivalente. Blant annet kan `[` og `{`, `]` og `}`, samt backslash og `|` sammenlignes likt. Tradisjonell `rfc1459` behandler også `^` og `~` likt; `strict-rfc1459` skiller disse.

Minimal-klienten har nå `irc_casefold()` og `irc_equal()`.

Dermed kan også avgjørelsen «var denne PRIVMSG-en sendt direkte til meg?» bruke IRC-regler i stedet for vanlig strengsammenligning.
