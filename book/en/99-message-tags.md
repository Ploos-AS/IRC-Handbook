# IRCv3 message tags

Message tags appear before the rest of an IRC message. The parser has supported generic tags for some time; `message_metadata()` now exposes common time, account, msgid and batch fields explicitly.

A missing tag is normal. Application code must not assume that metadata is present on every event.
