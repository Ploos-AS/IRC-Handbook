# M6.7: observerbar state engine

State engine har nå tre egenskaper som gjør den langt enklere å stole på og undervise med:

1. deterministiske snapshots
2. eksplisitte diffs
3. invariants under transcript-replay

Dette åpner for neste nivå av testing: et bibliotek av realistiske transcripts, fuzzing av parser/state-overgangen og property-baserte regler som «QUIT etterlater aldri samme nick i en kanal».

Vi trenger ikke gjøre eksempelboten til et fullverdig IRC-bibliotek. Målet er at leseren skal kunne se hvordan en robust protokollklient bygges lag for lag.
