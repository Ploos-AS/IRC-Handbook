# M6.6: en liten IRC state engine

Vi har nå beveget oss fra én kanal med en medlemsliste til en liten replaybar state engine:

```text
ServerFeatures
      ↓
ChannelRegistry
 ├─ #one → ChannelState
 ├─ #two → ChannelState
 └─ #... → ChannelState
             ↓
       NAMES generation
       + live events
```

Dette gir deterministisk multi-channel state, resync via NAMES og global håndtering av nickendringer og quits.

Det finnes fortsatt mer avanserte problemer i komplette IRC-klienter, men modellen er nå stor nok til å demonstrere arkitekturen uten at alle viktige state-problemer skjules bak et bibliotek.
