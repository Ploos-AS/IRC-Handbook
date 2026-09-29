# A safe CTCP reply policy

Automatic replies should be conservative. The example does not answer channel CTCP, never automatically answers CTCP carried in NOTICE, does not reply to ACTION, ignores unknown commands, and uses NOTICE for supported replies.

This reduces reply-loop risk and avoids turning the bot into an unnecessary response source. Being able to parse a request does not imply that software should answer it.
