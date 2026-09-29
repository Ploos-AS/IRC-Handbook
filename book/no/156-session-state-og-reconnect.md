# 156. Session-state og reconnect

En IRC-klient må skille mellom permanent konfigurasjon og state som bare gjelder én forbindelse.

Serverens ISUPPORT-verdier, aktuell nick, kanalmedlemmer og kanalmodi tilhører den aktive IRC-sessionen. Når TCP-forbindelsen forsvinner, er denne kunnskapen ikke lenger autoritativ.

Eksempelboten samler derfor denne informasjonen i `SessionState`. Hver reconnect oppretter en ny instans. Konfigurasjonen kan bestå, men server- og kanalstate starter på nytt.

Dette hindrer at medlemmer, kanalmodi eller serveregenskaper fra en gammel forbindelse blir behandlet som sannhet etter reconnect.
