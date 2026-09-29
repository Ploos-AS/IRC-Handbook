# The IRC message format

An IRC connection carries lines over a byte stream. A useful model is `[@tags ] [:prefix ] COMMAND [params] [:trailing] CRLF`.

Transport finds complete lines; the protocol parser then separates tags, source prefix, command and parameters. Application code should work with that structured representation rather than repeatedly splitting raw strings.
