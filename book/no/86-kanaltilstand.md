# Kanaltilstand som egen modell

En IRC-klient ser en strøm av hendelser. For å vise «hvordan kanalen ser ut nå» må den bygge lokal tilstand.

Eksempelklienten har derfor fått `ChannelState`.

Den holder rede på medlemmer, medlemsmodes, channel modes, modes med verdier og list modes. Protokollparseren forblir separat: først parses en melding, deretter anvendes hendelsen på state.

Denne delingen gjør modellen replaybar og testbar.
