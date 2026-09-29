import unittest
from irc_bot import AuthenticationError,Backoff,ServerError,StopFlag,encode_line,irc_casefold,irc_equal,is_numeric,parse_chanmodes,parse_isupport,parse_message,parse_prefix,response_for_line,sasl_plain
class BotTests(unittest.TestCase):
 def test_line_encoding(self):self.assertEqual(encode_line("PING :abc"),b"PING :abc\r\n")
 def test_rejects_injection(self):
  with self.assertRaises(ValueError):encode_line("X\r\nOPER bad")
 def test_parser(self):
  m=parse_message("@time=x;flag :n!u@h PRIVMSG #c :hello world")
  self.assertEqual((m.tags,m.prefix,m.command,m.params),({"time":"x","flag":None},"n!u@h","PRIVMSG",["#c","hello world"]))
 def test_middle_and_trailing_params(self):
  m=parse_message(":s COMMAND one two :three four")
  self.assertEqual(m.params,["one","two","three four"])
 def test_numeric_detection(self):
  self.assertTrue(is_numeric(parse_message(":s 005 b CHANTYPES=# :supported")))
  self.assertFalse(is_numeric(parse_message(":s PRIVMSG b :hello")))
 def test_isupport(self):
  m=parse_message(":s 005 b CHANTYPES=#& PREFIX=(ov)@+ CASEMAPPING=rfc1459 NICKLEN=30 :are supported")
  self.assertEqual(parse_isupport(m),{"CHANTYPES":"#&","PREFIX":"(ov)@+","CASEMAPPING":"rfc1459","NICKLEN":"30"})
 def test_isupport_boolean_and_removed(self):
  m=parse_message(":s 005 b SAFELIST -WHOX :are supported")
  self.assertEqual(parse_isupport(m),{"SAFELIST":True,"WHOX":False})
 def test_prefix(self):
  self.assertEqual(parse_prefix("(qaohv)~&@%+"),{"q":"~","a":"&","o":"@","h":"%","v":"+"})
  self.assertEqual(parse_prefix("(ov)@"),{})
 def test_chanmodes(self):
  self.assertEqual(parse_chanmodes("beI,k,l,imnst"),("beI","k","l","imnst"))
  self.assertEqual(parse_chanmodes("broken"),())
 def test_casemapping_ascii(self):
  self.assertTrue(irc_equal("Nick","NICK","ascii"))
  self.assertFalse(irc_equal("[","{","ascii"))
 def test_casemapping_rfc1459(self):
  self.assertTrue(irc_equal("[Nick]","{nick}","rfc1459"))
  self.assertTrue(irc_equal("^","~","rfc1459"))
 def test_casemapping_strict(self):
  self.assertTrue(irc_equal("[","{","strict-rfc1459"))
  self.assertFalse(irc_equal("^","~","strict-rfc1459"))
 def test_private_target_uses_irc_casefold(self):
  self.assertEqual(response_for_line(":a!u@h PRIVMSG {BOT} :!hello","[bot]","#c"),["PRIVMSG a :Hello, a!"])
 def test_ping(self):self.assertEqual(response_for_line("PING :s","b","#c"),["PONG :s"])
 def test_433(self):self.assertEqual(response_for_line(":s 433 * b :used","b","#c"),["NICK b_"])
 def test_error(self):
  with self.assertRaises(ServerError):response_for_line("ERROR :bye","b","#c")
 def test_required_sasl(self):
  with self.assertRaises(AuthenticationError):response_for_line(":s CAP b LS :multi-prefix","b","#c","a","p",True)
 def test_auth(self):self.assertEqual(response_for_line("AUTHENTICATE +","b","#c","a","p"),["AUTHENTICATE "+sasl_plain("a","p")])
 def test_backoff_sequence_and_cap(self):
  b=Backoff();self.assertEqual([b.next_delay() for _ in range(7)],[2,4,8,16,32,60,60])
 def test_backoff_reset(self):
  b=Backoff();b.next_delay();b.next_delay();b.reset();self.assertEqual(b.next_delay(),2)
 def test_stop_flag(self):
  s=StopFlag();self.assertFalse(s.requested);s.request();self.assertTrue(s.requested)
if __name__=="__main__":unittest.main()
