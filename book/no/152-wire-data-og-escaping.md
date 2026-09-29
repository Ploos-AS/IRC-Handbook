# 152. Wire-data og escaping

IRC inneholder kontrolltegn og escaping på flere nivåer. Det er lett å forveksle teksten `\\x01` med selve CTCP-tegnet byte 0x01, eller teksten `\\r\\n` med faktisk CRLF.

M6.10-testene konstruerer derfor kritiske wire-tegn eksplisitt. Det gjør skillet mellom Python-kildekode og data på IRC-forbindelsen synlig.

Samme regel gjelder IRCv3 message tags: unescaping må gjøres i én passering. Resultatet av én escape skal ikke tolkes på nytt som starten på en ny escape.
