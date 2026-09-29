import unittest
from irc_bot import AuthenticationError,ServerError,encode_line,parse_message,parse_privmsg,response_for_line,sasl_plain
class BotTests(unittest.TestCase):
 def test_line_encoding(self):self.assertEqual(encode_line("PING :abc"),b"PING :abc\r\n")
 def test_rejects_injection(self):
  with self.assertRaises(ValueError):encode_line("X\r\nOPER bad")
 def test_parser(self):
  m=parse_message("@time=x;flag :nick!u@h PRIVMSG #c :hello world")
  self.assertEqual((m.tags,m.prefix,m.command,m.params),({"time":"x","flag":None},"nick!u@h","PRIVMSG",["#c","hello world"]))
 def test_privmsg_tags(self):self.assertEqual(parse_privmsg("@a=b :n!u@h PRIVMSG #c :hi"),("n","#c","hi"))
 def test_ping(self):self.assertEqual(response_for_line("PING :s","b","#c"),["PONG :s"])
 def test_433_fallback(self):self.assertEqual(response_for_line(":s 433 * b :in use","b","#c"),["NICK b_"])
 def test_server_error(self):
  with self.assertRaises(ServerError):response_for_line("ERROR :Closing Link","b","#c")
 def test_cap_missing_optional(self):self.assertEqual(response_for_line(":s CAP b LS :multi-prefix","b","#c","a","p"),["CAP END"])
 def test_cap_missing_required(self):
  with self.assertRaises(AuthenticationError):response_for_line(":s CAP b LS :multi-prefix","b","#c","a","p",True)
 def test_cap_nak_required(self):
  with self.assertRaises(AuthenticationError):response_for_line(":s CAP b NAK :sasl","b","#c","a","p",True)
 def test_sasl_failure_optional(self):self.assertEqual(response_for_line(":s 904 b :failed","b","#c","a","p"),["CAP END"])
 def test_sasl_failure_required(self):
  with self.assertRaises(AuthenticationError):response_for_line(":s 904 b :failed","b","#c","a","p",True)
 def test_sasl_success(self):self.assertEqual(response_for_line(":s 903 b :ok","b","#c","a","p"),["CAP END"])
 def test_auth_payload(self):self.assertEqual(response_for_line("AUTHENTICATE +","b","#c","a","p"),["AUTHENTICATE "+sasl_plain("a","p")])
if __name__=="__main__":unittest.main()
