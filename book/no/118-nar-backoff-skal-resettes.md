# Når backoff skal resettes

Exponential backoff beskytter både klienten og serveren mot raske reconnect-looper.

En tidlig forbindelse som åpnes og lukkes igjen skal ikke nullstille backoff. Ellers kan en server som aksepterer TCP og umiddelbart lukker forbindelsen skape en reconnect-storm.

Backoff resettes derfor først etter en sesjon som faktisk har nådd healthy-state.
