import unittest
from irc_bot import AuthenticationError,Backoff,ChannelState,CtcpMessage,ModeChange,ServerError,StopFlag,ctcp_frame,encode_line,irc_casefold,irc_equal,is_numeric,parse_ctcp,parse_chanmodes,parse_isupport,parse_message,parse_mode_changes,parse_prefix,response_for_line,sasl_plain
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
 def test_member_mode_sequence(self):
  got=parse_mode_changes("+ov-v",["alice","bob","carol"],"ov",("beI","k","l","imnst"))
  self.assertEqual(got,[ModeChange(True,"o","alice"),ModeChange(True,"v","bob"),ModeChange(False,"v","carol")])
 def test_list_key_limit_and_flag_modes(self):
  cm=("beI","k","l","imnst")
  self.assertEqual(parse_mode_changes("+b-k+l+i",["*!*@bad","oldkey","50"],"ov",cm),
   [ModeChange(True,"b","*!*@bad"),ModeChange(False,"k","oldkey"),ModeChange(True,"l","50"),ModeChange(True,"i",None)])
 def test_unset_limit_needs_no_parameter(self):
  self.assertEqual(parse_mode_changes("-l",[],"ov",("beI","k","l","imnst")),[ModeChange(False,"l",None)])
 def test_mode_missing_parameter(self):
  with self.assertRaises(ValueError):parse_mode_changes("+o",[],"ov",("beI","k","l","imnst"))
 def test_mode_extra_parameter(self):
  with self.assertRaises(ValueError):parse_mode_changes("+i",["unused"],"ov",("beI","k","l","imnst"))
 def test_channel_state_lifecycle_and_modes(self):
  s=ChannelState("#Retro")
  for line in [":Alice!u@h JOIN #retro",":Bob!u@h JOIN #retro",":op!u@h MODE #retro +ov Alice Bob"]:
   s.apply(parse_message(line))
  self.assertEqual(s.members[s.key("alice")].modes,{"o"})
  self.assertEqual(s.members[s.key("BOB")].modes,{"v"})
  s.apply(parse_message(":Bob!u@h NICK Robert"))
  self.assertNotIn(s.key("Bob"),s.members);self.assertEqual(s.members[s.key("robert")].modes,{"v"})
  s.apply(parse_message(":op!u@h KICK #retro Robert :bye"))
  self.assertNotIn(s.key("Robert"),s.members)
 def test_channel_state_part_and_quit(self):
  s=ChannelState("#c")
  for line in [":a!u@h JOIN #c",":b!u@h JOIN #c",":a!u@h PART #c :bye",":b!u@h QUIT :gone"]:s.apply(parse_message(line))
  self.assertEqual(s.members,{})
 def test_channel_state_values_lists_flags(self):
  s=ChannelState("#c")
  s.apply(parse_message(":op MODE #c +klib secret 25 *!*@bad"))
  self.assertEqual(s.mode_values,{"k":"secret","l":"25"});self.assertIn("i",s.modes);self.assertEqual(s.lists["b"],{"*!*@bad"})
  s.apply(parse_message(":op MODE #c -k-l-b secret *!*@bad"))
  self.assertEqual(s.mode_values,{});self.assertEqual(s.lists["b"],set())
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
 def test_ctcp_parse_and_frame(self):
  self.assertEqual(parse_ctcp("\\x01ACTION waves\\x01"),CtcpMessage("ACTION","waves"))
  self.assertEqual(ctcp_frame("PING","123"),"\\x01PING 123\\x01")
  self.assertIsNone(parse_ctcp("ordinary text"))
 def test_ctcp_direct_version(self):
  self.assertEqual(response_for_line(":a!u@h PRIVMSG bot :\\x01VERSION\\x01","bot","#c"),
   ["NOTICE a :\\x01VERSION IRC Handbook educational bot\\x01"])
 def test_ctcp_ping_echoes_opaque_argument(self):
  self.assertEqual(response_for_line(":a!u@h PRIVMSG bot :\\x01PING 123 456\\x01","bot","#c"),
   ["NOTICE a :\\x01PING 123 456\\x01"])
 def test_ctcp_time_does_not_expose_clock(self):
  self.assertEqual(response_for_line(":a!u@h PRIVMSG bot :\\x01TIME\\x01","bot","#c"),
   ["NOTICE a :\\x01TIME not exposed by educational bot\\x01"])
 def test_ctcp_no_channel_or_notice_reply(self):
  self.assertEqual(response_for_line(":a!u@h PRIVMSG #c :\\x01VERSION\\x01","bot","#c"),[])
  self.assertEqual(response_for_line(":a!u@h NOTICE bot :\\x01VERSION x\\x01","bot","#c"),[])
 def test_ctcp_action_is_not_a_query(self):
  self.assertEqual(response_for_line(":a!u@h PRIVMSG bot :\\x01ACTION waves\\x01","bot","#c"),[])
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
