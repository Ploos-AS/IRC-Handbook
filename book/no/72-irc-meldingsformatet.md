# IRC-meldingsformatet

En IRC-forbindelse består av linjer over en byte-stream. En klassisk IRC-melding kan tenkes som:

```text
[@tags ] [:prefix ] COMMAND [params] [:trailing]\r\n
```

Ikke alle feltene finnes i alle meldinger.

Eksempel:

```text
:nick!user@host PRIVMSG #retro :Hei verden
```

gir:

```text
prefix  = nick!user@host
command = PRIVMSG
params  = ["#retro", "Hei verden"]
```

IRCv3 kan legge message tags foran resten:

```text
@time=... :nick!user@host PRIVMSG #retro :Hei
```

Transportlaget finner komplette linjer. Parseren deler deretter linjen i protokollfelt. Applikasjonen bør først arbeide med den strukturerte meldingen.
