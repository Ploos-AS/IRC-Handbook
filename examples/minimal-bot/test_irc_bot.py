import unittest
from irc_bot import encode_line,parse_message,parse_privmsg,response_for_line,sasl_plain

class BotTests(unittest.TestCase):
 def test_line_encoding(self): self.assertEqual(encode_line("PING :abc"),b"PING :abc\r\n")
 def test_rejects_injection(self):
  with self.assertRaises(ValueError): encode_line("X\r\nOPER bad")
 def test_structured_parser(self):
  m=parse_message("@time=2026-09-29T06:00:00Z;flag :nick!u@h PRIVMSG #c :hello world")
  self.assertEqual(m.tags,{"time":"2026-09-29T06:00:00Z","flag":None}); self.assertEqual(m.prefix,"nick!u@h")
  self.assertEqual(m.command,"PRIVMSG"); self.assertEqual(m.params,["#c","hello world"])
 def test_tag_unescape(self):
  self.assertEqual(parse_message("@x=hello\\sworld :s NOTICE n :x").tags["x"],"hello world")
 def test_privmsg_with_tags(self): self.assertEqual(parse_privmsg("@a=b :n!u@h PRIVMSG #c :hi"),("n","#c","hi"))
 def test_ping(self): self.assertEqual(response_for_line("PING :server","b","#c"),["PONG :server"])
 def test_welcome(self): self.assertEqual(response_for_line(":s 001 b :Welcome","b","#c"),["JOIN #c"])
 def test_hello(self): self.assertEqual(response_for_line(":a!u@h PRIVMSG #c :!hello","b","#c"),["PRIVMSG #c :Hello, a!"])
 def test_cap_ls_sasl(self): self.assertEqual(response_for_line(":s CAP b LS :multi-prefix sasl","b","#c","a","p"),["CAP REQ :sasl"])
 def test_cap_ls_without_sasl_ends(self): self.assertEqual(response_for_line(":s CAP b LS :multi-prefix","b","#c","a","p"),["CAP END"])
 def test_cap_ack(self): self.assertEqual(response_for_line(":s CAP b ACK :sasl","b","#c","a","p"),["AUTHENTICATE PLAIN"])
 def test_cap_nak(self): self.assertEqual(response_for_line(":s CAP b NAK :sasl","b","#c","a","p"),["CAP END"])
 def test_auth_plus(self): self.assertEqual(response_for_line("AUTHENTICATE +","b","#c","a","p"),["AUTHENTICATE "+sasl_plain("a","p")])
 def test_sasl_success(self): self.assertEqual(response_for_line(":s 903 b :ok","b","#c","a","p"),["CAP END"])
 def test_sasl_failure_ends_cap(self):
  for n in ("904","905","906","907"): self.assertEqual(response_for_line(f":s {n} b :failed","b","#c","a","p"),["CAP END"])
if __name__=="__main__":unittest.main()
