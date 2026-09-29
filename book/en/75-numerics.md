# Numerics

IRC servers frequently reply with three-digit numeric commands. We have already encountered 001 for successful registration, 005 for ISUPPORT, 433 for nickname-in-use, 903 for SASL success and 904–907 in SASL failure handling.

On the wire a numeric is still simply the command field. The example client now includes `is_numeric()` so higher layers can distinguish numeric replies from named commands such as PRIVMSG and PING.
