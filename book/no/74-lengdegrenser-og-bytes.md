# Lengdegrenser og bytes

IRC har historisk hatt en svært liten meldingsramme. Den klassiske grensen forbindes med 512 bytes inkludert linjeavslutningen.

Det viktige ordet er **bytes**, ikke tegn.

UTF-8 gjør forskjellen tydelig: ett synlig tegn kan bruke flere bytes.

Moderne IRC/IRCv3-miljøer kan tilby mekanismer eller serveregenskaper som påvirker hvor store meldinger en klient kan sende. En klient bør derfor ikke anta at «512 tegn» er riktig modell.

For undervisningsklienten holder vi foreløpig sendingene små og kontrollerte. Senere kan vi bruke serverens annonserte egenskaper når vi bygger en strengere serializer.
