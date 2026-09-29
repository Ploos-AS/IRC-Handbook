# Statusprefikser i NAMES

Et nick i NAMES kan ha statusprefikser:

```text
@Alice
+Bob
%+Helper
Plain
```

Prefiksene må ikke hardkodes til bare @ og +. Serverens ISUPPORT `PREFIX` forteller hvilke tegn som tilsvarer hvilke medlemsmodes.

Eksempelmodellen kan derfor lese flere samtidige statuser på samme medlem og lagrer dem som modes, for eksempel `{"h","v"}`.
