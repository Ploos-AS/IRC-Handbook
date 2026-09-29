# TCP, line framing og parsing

IRC er linjeorientert, men TCP er en byte-stream.

Det betyr at én `recv()` ikke nødvendigvis tilsvarer én IRC-melding.

Du kan få:

```text
recv #1: "PING :ab"
recv #2: "c\r\n:alice!u@h PRIV"
recv #3: "MSG #test :!hello\r\n"
```

Klienten må derfor bufferere bytes til en komplett linje finnes.

Eksempelbotens `iter_lines()` gjør nettopp dette.

## CRLF

IRC-linjer sendes avsluttet med CRLF:

```text
\r\n
```

Funksjonen `encode_line()` legger dette til og avviser data som allerede inneholder CR eller LF.

Det siste hindrer at en fremtidig funksjon ved et uhell gjør brukerinput om til ekstra IRC-kommandoer.

## Parseren

Den minimale parseren støtter bare det vi trenger nå.

Det er med vilje.

Senere utvider vi modellen med tags, prefix, capabilities og flere kommandoformer i stedet for å late som en enkel `split()` er en komplett IRC-parser.
