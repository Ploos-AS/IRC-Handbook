# State snapshots

Mutable runtime-state er praktisk internt, men dårlig som testgrensesnitt.

`channel_snapshot()` og `registry_snapshot()` lager derfor deterministiske datastrukturer med sorterte medlemmer, modes og lister. Snapshotet deler ikke mutable sets med den levende modellen.

Det kan dermed sammenlignes, serialiseres eller lagres som forventet testresultat uten at senere events endrer historikken.
