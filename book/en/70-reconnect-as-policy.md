# Reconnect as a separate policy

Reconnect backoff is now represented by a separate, testable `Backoff` component.

Its default sequence is `2, 4, 8, 16, 32, 60, 60 ...` seconds. It can be reset after a successful session and unit-tested without actually sleeping.

The main loop sleeps in short intervals so a termination signal can interrupt reconnect waiting promptly. The goal is to prevent reconnect storms without making shutdown sluggish.
