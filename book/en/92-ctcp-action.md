# CTCP ACTION and /me

When a user enters `/me waves`, an IRC client commonly sends a CTCP ACTION inside PRIVMSG. Receiving clients render it as an action rather than ordinary chat.

ACTION is not a query that our bot should answer. The example parses it but produces no automatic reply. This illustrates the important distinction between understanding a protocol message and deciding to react to it.
