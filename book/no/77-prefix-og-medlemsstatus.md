# PREFIX og medlemsstatus

IRC-klienter viser ofte symboler foran nick i en kanal, for eksempel `@` eller `+`.

Serveren kan beskrive sammenhengen gjennom ISUPPORT:

```text
PREFIX=(ov)@+
```

Dette betyr at mode `o` vises som `@`, mens mode `v` vises som `+`.

Nettverk kan annonsere flere nivåer:

```text
PREFIX=(qaohv)~&@%+
```

Klienten bør derfor ikke anta at bare operator og voice finnes.

Minimal-klienten har nå `parse_prefix()`, som gjør PREFIX til en eksplisitt mode→symbol-tabell.
