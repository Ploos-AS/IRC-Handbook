# Reconfigure når serverregler endres

Når nye 005-data mottas, re-konfigurerer registry eksisterende kanalmodeller med aktuell CASEMAPPING, PREFIX og CHANMODES.

Registry bygger samtidig kanalindeksen på nytt med den aktive casemappingen.

Dette holder protokollreglene samlet i `ServerFeatures` og hindrer at hver kanal utvikler sin egen kopi av serverkonfigurasjonen.
