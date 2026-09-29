# PREFIX and membership status

IRC clients commonly display symbols such as @ or + before nicknames in a channel. ISUPPORT can define that mapping with values such as `PREFIX=(ov)@+` or richer forms like `PREFIX=(qaohv)~&@%+`.

Clients should therefore not assume that only operator and voice status exist. The minimal client now includes `parse_prefix()`, producing an explicit mode-to-symbol mapping.
