# Deterministisk transcript-replay

`replay_transcript()` tar rå IRC-linjer, parser dem og spiller dem gjennom ServerFeatures og ChannelRegistry i samme rekkefølge.

Dermed kan en test beskrives som:

```text
IRC transcript
      ↓
 parser
      ↓
 state engine
      ↓
 snapshot
```

Samme input skal gi samme slutt-state. Dette gjør virkelige protokollsekvenser til gode regresjonstester.
