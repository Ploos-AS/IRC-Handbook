import unittest

from irc_bot import encode_line, parse_privmsg, response_for_line


class BotTests(unittest.TestCase):
    def test_line_encoding(self):
        self.assertEqual(encode_line("PING :abc"), b"PING :abc\r\n")

    def test_rejects_line_injection(self):
        with self.assertRaises(ValueError):
            encode_line("PRIVMSG #x :hello\r\nOPER bad")

    def test_ping_pong(self):
        self.assertEqual(
            response_for_line("PING :server.example", "bot", "#test"),
            ["PONG :server.example"],
        )

    def test_join_after_welcome(self):
        self.assertEqual(
            response_for_line(":srv 001 bot :Welcome", "bot", "#test"),
            ["JOIN #test"],
        )

    def test_channel_hello(self):
        self.assertEqual(
            response_for_line(":alice!u@h PRIVMSG #test :!hello", "bot", "#test"),
            ["PRIVMSG #test :Hello, alice!"],
        )

    def test_private_hello(self):
        self.assertEqual(
            response_for_line(":alice!u@h PRIVMSG bot :!hello", "bot", "#test"),
            ["PRIVMSG alice :Hello, alice!"],
        )

    def test_ordinary_message_ignored(self):
        self.assertEqual(
            response_for_line(":alice!u@h PRIVMSG #test :hello", "bot", "#test"),
            [],
        )

    def test_parse_privmsg(self):
        self.assertEqual(
            parse_privmsg(":nick!user@host PRIVMSG #chan :hello world"),
            ("nick", "#chan", "hello world"),
        )


if __name__ == "__main__":
    unittest.main()
