import pathlib,socket,threading,time,unittest
from irc_bot import AuthenticationError,Backoff,CapabilityState,assert_registry_invariants,ConnectionClosed,ChannelRegistry,ChannelState,Negotiation,channel_snapshot,CtcpMessage,Member,ModeChange,ServerError,ServerFeatures,SessionResult,StopFlag,ctcp_frame,encode_line,irc_casefold,irc_equal,is_numeric,message_metadata,mutate_transcript,parse_capabilities,parse_ctcp,parse_chanmodes,parse_isupport,parse_message,parse_mode_changes,parse_prefix,registry_snapshot,replay_transcript,response_for_line,sasl_authenticate_lines,sasl_plain,snapshot_diff,iter_lines
class BotTests(unittest.TestCase):
 def test_line_encoding(self):self.assertEqual(encode_line("PING :abc"),b"PING :abc\r\n")
 def test_rejects_injection(self):
  with self.assertRaises(ValueError):encode_line("X\r\nOPER bad")
 def test_tag_unescape_is_single_pass(self):
  self.assertEqual(parse_message("@x=one\\\\stwo\\:three\\q :s CMD").tags["x"],"one\\stwo;threeq")
 def test_tag_unescape_does_not_decode_generated_escape(self):
  self.assertEqual(parse_message("@x=\\\\s CMD").tags["x"],r"\s")
 def test_tag_unescape_unknown_escape_drops_only_backslash(self):
  self.assertEqual(parse_message(r"@x=a\qb CMD").tags["x"],"aqb")
 def test_tag_unescape_trailing_backslash_is_dropped(self):
  self.assertEqual(parse_message("@x=value\\\\ CMD").tags["x"],"value\\")
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
 def test_server_features_accumulate_and_remove(self):
  f=ServerFeatures()
  f.update(parse_message(":s 005 b CASEMAPPING=ascii PREFIX=(qaohv)~&@%+ :supported"))
  f.update(parse_message(":s 005 b CHANMODES=beI,k,l,imnst -PREFIX :supported"))
  self.assertEqual(f.casemapping,"ascii");self.assertEqual(f.prefix,{"o":"@","v":"+"})
  self.assertEqual(f.chanmodes,("beI","k","l","imnst"))
 def test_server_features_unknown_casemapping_falls_back(self):
  f=ServerFeatures({"CASEMAPPING":"future-map"})
  self.assertEqual(f.casemapping,"rfc1459")
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
 def corpus(self,name):
  return (pathlib.Path(__file__).with_name("transcripts")/name).read_text().splitlines()
 def test_corpus_names_modes(self):
  snap=registry_snapshot(replay_transcript(self.corpus("names-modes.irc")))
  self.assertEqual(snap["#retro"]["members"]["bob"]["modes"],["h","o","v"])
  self.assertIn("alicia",snap["#retro"]["members"]);self.assertNotIn("plain",snap["#retro"]["members"])
 def test_corpus_multichannel_global_events(self):
  snap=registry_snapshot(replay_transcript(self.corpus("multichannel.irc")))
  self.assertIn("alicia",snap["#one"]["members"]);self.assertIn("alicia",snap["#two"]["members"])
  self.assertNotIn("carol",snap["#two"]["members"])
 def test_corpus_resync_removes_stale_preserves_interleaved_join(self):
  snap=registry_snapshot(replay_transcript(self.corpus("resync.irc")));members=snap["#sync"]["members"]
  self.assertNotIn("old",members);self.assertIn("late",members);self.assertIn("during",members)
 def test_seeded_mutations_preserve_invariants_when_parseable(self):
  lines=self.corpus("multichannel.irc");seen=0
  for mutated in mutate_transcript(lines,seed=20260929,rounds=64):
   try:r=replay_transcript(mutated)
   except ValueError:continue
   self.assertTrue(assert_registry_invariants(r));seen+=1
  self.assertGreater(seen,0)
 def test_quit_property_removes_nick_from_every_channel(self):
  lines=self.corpus("multichannel.irc")+[":Alicia!u@h QUIT :gone"]
  snap=registry_snapshot(replay_transcript(lines))
  self.assertTrue(all("alicia" not in channel["members"] for channel in snap.values()))
 def test_transcript_replay_is_deterministic(self):
  lines=[":s 005 bot CASEMAPPING=ascii PREFIX=(ov)@+ CHANMODES=beI,k,l,imnst :supported",
   ":s 353 bot = #one :@Alice +Bob",":s 366 bot #one :End",":op!u@h MODE #one +o Bob",":Alice!u@h NICK Alicia"]
  a=registry_snapshot(replay_transcript(lines));b=registry_snapshot(replay_transcript(lines))
  self.assertEqual(a,b);self.assertEqual(a["#one"]["members"]["bob"]["modes"],["o","v"])
 def test_snapshot_is_detached_from_mutable_state(self):
  s=ChannelState("#c");s.add_member("Alice",{"o"});snap=channel_snapshot(s);s.members[s.key("Alice")].modes.add("v")
  self.assertEqual(snap["members"][s.key("Alice")]["modes"],["o"])
 def test_snapshot_diff_channels(self):
  self.assertEqual(snapshot_diff({"#a":{"x":1}},{"#a":{"x":2},"#b":{}}),{"added":["#b"],"removed":[],"changed":["#a"]})
 def test_registry_invariant_detects_bad_member_key(self):
  r=ChannelRegistry(ServerFeatures());s=r.get("#c");s.members["wrong"]=Member("Alice",set())
  with self.assertRaises(AssertionError):assert_registry_invariants(r)
 def test_names_generation_removes_stale_members(self):
  s=ChannelState("#c");s.add_member("Stale")
  s.apply(parse_message(":s 353 bot = #c :@Alice Bob"),{"o":"@","v":"+"})
  self.assertIn(s.key("Stale"),s.members)
  s.apply(parse_message(":s 366 bot #c :End"),{"o":"@","v":"+"})
  self.assertNotIn(s.key("Stale"),s.members);self.assertIn(s.key("Alice"),s.members)
 def test_event_during_names_survives_snapshot_end(self):
  s=ChannelState("#c")
  s.apply(parse_message(":s 353 bot = #c :Alice"),{"o":"@","v":"+"})
  s.apply(parse_message(":Late!u@h JOIN #c"),{"o":"@","v":"+"})
  s.names_seen.add(s.key("Late"))
  s.apply(parse_message(":s 366 bot #c :End"),{"o":"@","v":"+"})
  self.assertIn(s.key("Late"),s.members)
 def test_registry_routes_multiple_channels(self):
  f=ServerFeatures({"CASEMAPPING":"ascii","PREFIX":"(ov)@+","CHANMODES":"beI,k,l,imnst"});r=ChannelRegistry(f)
  for line in [":s 353 bot = #one :@Alice",":s 366 bot #one :End",":s 353 bot = #two :+Bob",":s 366 bot #two :End"]:
   r.apply(parse_message(line))
  self.assertIn(r.get("#one").key("Alice"),r.get("#one").members)
  self.assertNotIn(r.get("#one").key("Bob"),r.get("#one").members)
  self.assertIn(r.get("#two").key("Bob"),r.get("#two").members)
 def test_registry_global_nick_and_quit(self):
  f=ServerFeatures();r=ChannelRegistry(f)
  for ch in ("#a","#b"):r.get(ch).add_member("Alice")
  r.apply(parse_message(":Alice!u@h NICK Alicia"))
  self.assertTrue(all(s.key("Alicia") in s.members for s in r.channels.values()))
  r.apply(parse_message(":Alicia!u@h QUIT :gone"))
  self.assertTrue(all(not s.members for s in r.channels.values()))
 def test_names_replay_with_dynamic_prefixes(self):
  f=ServerFeatures();f.update(parse_message(":s 005 bot CASEMAPPING=ascii PREFIX=(qaohv)~&@%+ CHANMODES=beI,k,l,imnst :supported"))
  s=ChannelState("#c");s.configure(f)
  s.apply(parse_message(":s 353 bot = #c :~Owner @Op %+Helper Plain"),f.prefix)
  self.assertEqual(s.members[s.key("Owner")].modes,{"q"})
  self.assertEqual(s.members[s.key("Op")].modes,{"o"})
  self.assertEqual(s.members[s.key("Helper")].modes,{"h","v"})
  self.assertEqual(s.members[s.key("Plain")].modes,set())
 def test_names_then_live_mode_and_nick(self):
  f=ServerFeatures({"PREFIX":"(ov)@+","CHANMODES":"beI,k,l,imnst"})
  s=ChannelState("#c");s.configure(f)
  for line in [":s 353 bot = #c :@Alice +Bob",":s 366 bot #c :End",":op MODE #c +o Bob",":Alice!u@h NICK Alicia"]:
   s.apply(parse_message(line),f.prefix)
  self.assertEqual(s.members[s.key("Bob")].modes,{"o","v"})
  self.assertEqual(s.members[s.key("Alicia")].modes,{"o"})
 def test_channel_state_configures_ascii_mapping(self):
  f=ServerFeatures({"CASEMAPPING":"ascii"});s=ChannelState("#c");s.configure(f);s.add_member("[Nick]")
  self.assertIn(s.key("[nick]"),s.members);self.assertNotEqual(s.key("[nick]"),s.key("{nick}"))
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
 def test_action_mapping_can_be_server_selected(self):
  m=parse_message(":a!u@h PRIVMSG {BOT} :!hello")
  from irc_bot import actions_for_message
  self.assertEqual(actions_for_message(m,"[bot]","#c",case_mapping="ascii"),["PRIVMSG {BOT} :Hello, a!"])
  self.assertEqual(actions_for_message(m,"[bot]","#c",case_mapping="rfc1459"),["PRIVMSG a :Hello, a!"])
 def test_ctcp_parse_and_frame(self):
  self.assertEqual(parse_ctcp("\x01ACTION waves\x01"),CtcpMessage("ACTION","waves"))
  self.assertEqual(ctcp_frame("PING","123"),"\x01PING 123\x01")
  self.assertIsNone(parse_ctcp("ordinary text"))
 def test_ctcp_direct_version(self):
  self.assertEqual(response_for_line(":a!u@h PRIVMSG bot :\\x01VERSION\x01","bot","#c"),
   ["NOTICE a :\\x01VERSION IRC Handbook educational bot\x01"])
 def test_ctcp_ping_echoes_opaque_argument(self):
  self.assertEqual(response_for_line(":a!u@h PRIVMSG bot :\\x01PING 123 456\x01","bot","#c"),
   ["NOTICE a :\\x01PING 123 456\x01"])
 def test_ctcp_time_does_not_expose_clock(self):
  self.assertEqual(response_for_line(":a!u@h PRIVMSG bot :\\x01TIME\x01","bot","#c"),
   ["NOTICE a :\\x01TIME not exposed by educational bot\x01"])
 def test_ctcp_no_channel_or_notice_reply(self):
  self.assertEqual(response_for_line(":a!u@h PRIVMSG #c :\\x01VERSION\x01","bot","#c"),[])
  self.assertEqual(response_for_line(":a!u@h NOTICE bot :\\x01VERSION x\x01","bot","#c"),[])
 def test_ctcp_action_is_not_a_query(self):
  self.assertEqual(response_for_line(":a!u@h PRIVMSG bot :\\x01ACTION waves\x01","bot","#c"),[])
 def test_capability_values(self):
  self.assertEqual(parse_capabilities("sasl=PLAIN,EXTERNAL server-time account-tag"),{"sasl":"PLAIN,EXTERNAL","server-time":None,"account-tag":None})
 def test_cap_ls_continuation(self):
  s=CapabilityState()
  s.apply(parse_message(":s CAP b LS * :multi-prefix sasl=PLAIN"))
  self.assertEqual(s.available,{})
  s.apply(parse_message(":s CAP b LS :server-time account-tag"))
  self.assertEqual(s.available,{"multi-prefix":None,"sasl":"PLAIN","server-time":None,"account-tag":None})
 def test_cap_new_del_ack(self):
  s=CapabilityState()
  s.apply(parse_message(":s CAP b NEW :echo-message=1 draft/test"))
  s.apply(parse_message(":s CAP b ACK :echo-message draft/test"))
  self.assertEqual(s.enabled,{"echo-message","draft/test"})
  s.apply(parse_message(":s CAP b DEL :draft/test"))
  self.assertNotIn("draft/test",s.available);self.assertNotIn("draft/test",s.enabled)
 def test_message_metadata(self):
  m=parse_message("@time=2026-09-29T10:00:00.000Z;account=alice;msgid=abc;batch=42 :a!u@h PRIVMSG #c :hi")
  self.assertEqual(message_metadata(m),{"time":"2026-09-29T10:00:00.000Z","account":"alice","msgid":"abc","batch":"42"})
 def test_negotiation_waits_for_final_ls(self):
  n=Negotiation(True,True)
  self.assertEqual(n.actions(parse_message(":s CAP b LS * :server-time account-tag")),[])
  self.assertEqual(n.actions(parse_message(":s CAP b LS :sasl=PLAIN message-tags")),["CAP REQ :server-time account-tag message-tags sasl"])
 def test_negotiation_without_sasl(self):
  n=Negotiation()
  self.assertEqual(n.actions(parse_message(":s CAP b LS :server-time sasl account-tag")),["CAP REQ :server-time account-tag"])
 def test_negotiation_ack_sasl_starts_auth(self):
  n=Negotiation(True,True)
  n.actions(parse_message(":s CAP b LS :sasl server-time"))
  self.assertEqual(n.actions(parse_message(":s CAP b ACK :server-time sasl")),["AUTHENTICATE PLAIN"])
 def test_negotiation_ack_without_sasl_ends_cap(self):
  n=Negotiation()
  n.actions(parse_message(":s CAP b LS :server-time"))
  self.assertEqual(n.actions(parse_message(":s CAP b ACK :server-time")),["CAP END"])
 def test_negotiation_required_sasl_missing(self):
  n=Negotiation(True,True)
  with self.assertRaises(AuthenticationError):n.actions(parse_message(":s CAP b LS :server-time"))
 def test_ping(self):self.assertEqual(response_for_line("PING :s","b","#c"),["PONG :s"])
 def test_433(self):self.assertEqual(response_for_line(":s 433 * b :used","b","#c"),["NICK b_"])
 def test_error(self):
  with self.assertRaises(ServerError):response_for_line("ERROR :bye","b","#c")
 def test_cap_without_negotiation_has_no_stateless_fallback(self):
  self.assertEqual(response_for_line(":s CAP b LS :sasl","b","#c","a","p",True),[])
 def test_response_helper_can_use_stateful_negotiation(self):
  n=Negotiation(True,True)
  self.assertEqual(response_for_line(":s CAP b LS :sasl server-time","b","#c","a","p",True,n),["CAP REQ :server-time sasl"])
 def test_auth(self):self.assertEqual(response_for_line("AUTHENTICATE +","b","#c","a","p"),["AUTHENTICATE "+sasl_plain("a","p")])
 def test_sasl_authenticate_chunking(self):
  lines=sasl_authenticate_lines("u","p"*600)
  self.assertTrue(all(len(x.removeprefix("AUTHENTICATE "))<=400 for x in lines))
  self.assertGreater(len(lines),1)
 def test_sasl_exact_chunk_gets_terminator(self):
  password="p"
  while len(sasl_plain("u",password))%400:password+="p"
  self.assertEqual(sasl_authenticate_lines("u",password)[-1],"AUTHENTICATE +")
 def test_iter_lines_stops_while_peer_is_silent(self):
  left,right=socket.socketpair();stop=StopFlag();done=[]
  def consume():done.extend(iter_lines(left,stop,.02))
  th=threading.Thread(target=consume);th.start();time.sleep(.04);stop.request();th.join(.3)
  right.close();left.close();self.assertFalse(th.is_alive());self.assertEqual(done,[])
 def test_iter_lines_handles_fragmentation(self):
  left,right=socket.socketpair();right.sendall(b"PING :a\r");right.sendall(b"\nPING :b\r\n");right.shutdown(socket.SHUT_WR)
  self.assertEqual(list(iter_lines(left,poll_timeout=.02)),["PING :a","PING :b"]);right.close();left.close()
 def test_session_result_distinguishes_health_and_stop(self):
  self.assertEqual(SessionResult(False,False),SessionResult(False))
  self.assertTrue(SessionResult(True,True).healthy);self.assertTrue(SessionResult(True,True).stopped)
 def test_connection_closed_is_session_error(self):
  self.assertTrue(issubclass(ConnectionClosed,Exception))
 def test_backoff_sequence_and_cap(self):
  b=Backoff();self.assertEqual([b.next_delay() for _ in range(7)],[2,4,8,16,32,60,60])
 def test_backoff_reset(self):
  b=Backoff();b.next_delay();b.next_delay();b.reset();self.assertEqual(b.next_delay(),2)
 def test_stop_flag(self):
  s=StopFlag();self.assertFalse(s.requested);s.request();self.assertTrue(s.requested)
if __name__=="__main__":unittest.main()
