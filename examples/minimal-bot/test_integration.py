import socket, threading, unittest
from irc_bot import Config, run_session, sasl_plain

def recv_line(conn, buf=b""):
    while b"\n" not in buf:
        chunk=conn.recv(4096)
        if not chunk: raise EOFError("connection closed")
        buf+=chunk
    raw,buf=buf.split(b"\n",1)
    return raw.rstrip(b"\r").decode(),buf

class FakeIRCServer:
    def __init__(self, sasl=False):
        self.sasl=sasl; self.transcript=[]; self.error=None
        self.listener=socket.socket(); self.listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.listener.bind(("127.0.0.1",0)); self.listener.listen(1)
        self.host,self.port=self.listener.getsockname()
        self.thread=threading.Thread(target=self._serve,daemon=True)
    def start(self): self.thread.start()
    def join(self):
        self.thread.join(5); self.listener.close()
        if self.thread.is_alive(): raise TimeoutError("fake IRC server did not finish")
        if self.error: raise self.error
    def read(self,c,b):
        line,b=recv_line(c,b); self.transcript.append(line); return line,b
    def expect(self,c,b,want):
        got,b=self.read(c,b)
        if got!=want: raise AssertionError(f"{got!r} != {want!r}")
        return b
    def _serve(self):
        try:
            c,_=self.listener.accept(); c.settimeout(3)
            with c:
                b=b""
                if self.sasl: b=self.expect(c,b,"CAP LS 302")
                b=self.expect(c,b,"NICK handbookbot")
                b=self.expect(c,b,"USER handbookbot 0 * :IRC Handbook Bot")
                if self.sasl:
                    c.sendall(b":fake CAP handbookbot LS :multi-prefix sasl\r\n")
                    b=self.expect(c,b,"CAP REQ :sasl")
                    c.sendall(b":fake CAP handbookbot ACK :sasl\r\n")
                    b=self.expect(c,b,"AUTHENTICATE PLAIN")
                    c.sendall(b"AUTHENTICATE +\r\n")
                    b=self.expect(c,b,"AUTHENTICATE "+sasl_plain("acct","secret"))
                    c.sendall(b":fake 903 handbookbot :SASL authentication successful\r\n")
                    b=self.expect(c,b,"CAP END")
                c.sendall(b":fake 001 handbookbot :Wel"); c.sendall(b"come\r\n")
                b=self.expect(c,b,"JOIN #handbook-test")
                c.sendall(b"PING :integration-token\r\n")
                b=self.expect(c,b,"PONG :integration-token")
                c.sendall(b":alice!u@h PRIVMSG #handbook-test :!hel"); c.sendall(b"lo\r\n")
                b=self.expect(c,b,"PRIVMSG #handbook-test :Hello, alice!")
        except Exception as e: self.error=e

class IntegrationTests(unittest.TestCase):
    def run_case(self,sasl):
        s=FakeIRCServer(sasl); s.start()
        cfg=Config(s.host,s.port,"handbookbot","#handbook-test",False,
                   "acct" if sasl else None,"secret" if sasl else None)
        run_session(cfg); s.join(); return s
    def test_complete_plaintext_local_session(self): self.run_case(False)
    def test_complete_sasl_cap_session(self): self.run_case(True)

if __name__=="__main__": unittest.main()
