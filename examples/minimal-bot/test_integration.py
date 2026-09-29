import socket
import threading
import unittest

from irc_bot import Config, run_session


def recv_line(conn, buf=b""):
    while b"\n" not in buf:
        chunk = conn.recv(4096)
        if not chunk:
            raise EOFError("connection closed before a complete line")
        buf += chunk
    raw, buf = buf.split(b"\n", 1)
    return raw.rstrip(b"\r").decode("utf-8"), buf


class FakeIRCServer:
    def __init__(self):
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listener.bind(("127.0.0.1", 0))
        self.listener.listen(1)
        self.host, self.port = self.listener.getsockname()
        self.transcript = []
        self.error = None
        self.thread = threading.Thread(target=self._serve, daemon=True)

    def start(self):
        self.thread.start()

    def join(self):
        self.thread.join(timeout=5)
        self.listener.close()
        if self.thread.is_alive():
            raise TimeoutError("fake IRC server did not finish")
        if self.error:
            raise self.error

    def _read(self, conn, buf):
        line, buf = recv_line(conn, buf)
        self.transcript.append(line)
        return line, buf

    def _serve(self):
        try:
            conn, _ = self.listener.accept()
            conn.settimeout(3)
            with conn:
                buf = b""
                first, buf = self._read(conn, buf)
                second, buf = self._read(conn, buf)
                if not first.startswith("NICK "):
                    raise AssertionError(first)
                if not second.startswith("USER "):
                    raise AssertionError(second)

                # Deliberately fragment the welcome line across TCP writes.
                conn.sendall(b":fake.example 001 handbookbot :Wel")
                conn.sendall(b"come to the test server\r\n")

                join, buf = self._read(conn, buf)
                if join != "JOIN #handbook-test":
                    raise AssertionError(join)

                # Exercise PING/PONG.
                conn.sendall(b"PING :integration-token\r\n")
                pong, buf = self._read(conn, buf)
                if pong != "PONG :integration-token":
                    raise AssertionError(pong)

                # Exercise a fragmented PRIVMSG and command response.
                conn.sendall(b":alice!u@h PRIVMSG #handbook-test :!hel")
                conn.sendall(b"lo\r\n")
                reply, buf = self._read(conn, buf)
                expected = "PRIVMSG #handbook-test :Hello, alice!"
                if reply != expected:
                    raise AssertionError(reply)
        except Exception as exc:
            self.error = exc


class IntegrationTests(unittest.TestCase):
    def test_complete_plaintext_local_session(self):
        server = FakeIRCServer()
        server.start()

        config = Config(
            host=server.host,
            port=server.port,
            nick="handbookbot",
            channel="#handbook-test",
            use_tls=False,
        )

        # Plaintext is allowed only here because this socket is loopback-only
        # and exists solely as a deterministic protocol test.
        run_session(config)
        server.join()

        self.assertEqual(
            server.transcript,
            [
                "NICK handbookbot",
                "USER handbookbot 0 * :IRC Handbook Bot",
                "JOIN #handbook-test",
                "PONG :integration-token",
                "PRIVMSG #handbook-test :Hello, alice!",
            ],
        )


if __name__ == "__main__":
    unittest.main()
