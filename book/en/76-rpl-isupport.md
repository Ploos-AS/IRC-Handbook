# 005 RPL_ISUPPORT

005 RPL_ISUPPORT lets a server describe properties of the IRC environment the client actually joined.

Tokens such as `CHANTYPES=#&`, `PREFIX=(ov)@+`, `CASEMAPPING=rfc1459` and `NICKLEN=30` communicate rules that clients should not blindly hard-code. Some tokens are boolean features, while a leading `-` can remove a previously advertised feature.

The minimal client now includes `parse_isupport()` to demonstrate turning those tokens into structured data.
