import unittest
from irc_bot import encode_line, parse_privmsg, response_for_line, sasl_plain

class BotTests(unittest.TestCase):
    def test_line_encoding(self):
        self.assertEqual(encode_line("PING :abc"), b"PING :abc\r\n")
    def test_rejects_line_injection(self):
        with self.assertRaises(ValueError): encode_line("PRIVMSG #x :hello\r\nOPER bad")
    def test_ping_pong(self):
        self.assertEqual(response_for_line("PING :server.example","bot","#test"),["PONG :server.example"])
    def test_join_after_welcome(self):
        self.assertEqual(response_for_line(":srv 001 bot :Welcome","bot","#test"),["JOIN #test"])
    def test_channel_hello(self):
        self.assertEqual(response_for_line(":alice!u@h PRIVMSG #test :!hello","bot","#test"),["PRIVMSG #test :Hello, alice!"])
    def test_private_hello(self):
        self.assertEqual(response_for_line(":alice!u@h PRIVMSG bot :!hello","bot","#test"),["PRIVMSG alice :Hello, alice!"])
    def test_ordinary_message_ignored(self):
        self.assertEqual(response_for_line(":alice!u@h PRIVMSG #test :hello","bot","#test"),[])
    def test_parse_privmsg(self):
        self.assertEqual(parse_privmsg(":nick!user@host PRIVMSG #chan :hello world"),("nick","#chan","hello world"))
    def test_cap_ls_requests_sasl(self):
        self.assertEqual(response_for_line(":srv CAP bot LS :multi-prefix sasl","bot","#x","acct","secret"),["CAP REQ :sasl"])
    def test_cap_ack_starts_plain(self):
        self.assertEqual(response_for_line(":srv CAP bot ACK :sasl","bot","#x","acct","secret"),["AUTHENTICATE PLAIN"])
    def test_authenticate_plus_sends_payload(self):
        self.assertEqual(response_for_line("AUTHENTICATE +","bot","#x","acct","secret"),["AUTHENTICATE "+sasl_plain("acct","secret")])
    def test_sasl_success_ends_cap(self):
        self.assertEqual(response_for_line(":srv 903 bot :SASL authentication successful","bot","#x","acct","secret"),["CAP END"])
    def test_plain_payload(self):
        self.assertEqual(sasl_plain("acct","secret"),"AGFjY3QAc2VjcmV0")

if __name__ == "__main__": unittest.main()
