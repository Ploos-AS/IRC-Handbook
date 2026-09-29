import socket,threading,time,unittest
from irc_bot import AuthenticationError,Config,ConnectionClosed,ServerError,SessionResult,StopFlag,run_session,sasl_plain,validate
def recv_line(c,b=b""):
 while b"\n" not in b:
  x=c.recv(4096)
  if not x:raise EOFError("connection closed")
  b+=x
 raw,b=b.split(b"\n",1);return raw.rstrip(b"\r").decode(),b
class Fake:
 def __init__(self,mode):
  self.mode=mode;self.error=None;self.listener=socket.socket();self.listener.bind(("127.0.0.1",0));self.listener.listen(1)
  self.host,self.port=self.listener.getsockname();self.thread=threading.Thread(target=self.serve,daemon=True)
 def start(self):self.thread.start()
 def join(self):
  self.thread.join(5);self.listener.close()
  if self.thread.is_alive():raise TimeoutError()
  if self.error:raise self.error
 def expect(self,c,b,w):
  got,b=recv_line(c,b)
  if got!=w:raise AssertionError((got,w))
  return b
 def serve(self):
  try:
   c,_=self.listener.accept();c.settimeout(3)
   with c:
    b=b""
    b=self.expect(c,b,"CAP LS 302")
    b=self.expect(c,b,"NICK handbookbot");b=self.expect(c,b,"USER handbookbot 0 * :IRC Handbook Bot")
    if self.mode=="names":
     c.sendall(b":s CAP handbookbot LS :server-time\r\n");b=self.expect(c,b,"CAP REQ :server-time")
     c.sendall(b":s CAP handbookbot ACK :server-time\r\n");b=self.expect(c,b,"CAP END")
     c.sendall(b":s 005 handbookbot CASEMAPPING=ascii PREFIX=(ohv)@%+ CHANMODES=beI,k,l,imnst :supported\r\n")
     c.sendall(b":s 001 handbookbot :Welcome\r\n");b=self.expect(c,b,"JOIN #handbook-test")
     c.sendall(b":s 353 handbookbot = #handbook-test :@Alice %+Bob Plain\r\n:s 366 handbookbot #handbook-test :End\r\n")
     c.sendall(b":op!u@h MODE #handbook-test +o Bob\r\n");return
    if self.mode=="plain":
     c.sendall(b":s CAP handbookbot LS :server-time\r\n");b=self.expect(c,b,"CAP REQ :server-time")
     c.sendall(b":s CAP handbookbot ACK :server-time\r\n");b=self.expect(c,b,"CAP END")
     c.sendall(b":s 001 handbookbot :Welcome\r\n");b=self.expect(c,b,"JOIN #handbook-test");return
    if self.mode=="stop":
     c.sendall(b":s CAP handbookbot LS :server-time\r\n");b=self.expect(c,b,"CAP REQ :server-time")
     c.sendall(b":s CAP handbookbot ACK :server-time\r\n");b=self.expect(c,b,"CAP END")
     b=self.expect(c,b,"QUIT :Shutting down");return
    if self.mode=="nick":
     c.sendall(b":s 433 * handbookbot :in use\r\n");b=self.expect(c,b,"NICK handbookbot_");return
    if self.mode=="error":c.sendall(b"ERROR :maintenance\r\n");return
    if self.mode=="missing":
     c.sendall(b":s CAP handbookbot LS :multi-prefix\r\n");return
    if self.mode=="fail":
     c.sendall(b":s CAP handbookbot LS :sasl\r\n");b=self.expect(c,b,"CAP REQ :sasl")
     c.sendall(b":s CAP handbookbot ACK :sasl\r\n");b=self.expect(c,b,"AUTHENTICATE PLAIN")
     c.sendall(b"AUTHENTICATE +\r\n");b=self.expect(c,b,"AUTHENTICATE "+sasl_plain("acct","secret"))
     c.sendall(b":s 904 handbookbot :failed\r\n");return
    c.sendall(b":s 001 handbookbot :Welcome\r\n");b=self.expect(c,b,"JOIN #handbook-test")
  except Exception as e:self.error=e
class IntegrationTests(unittest.TestCase):
 def cfg(self,s,required=False,sasl=False):return Config(s.host,s.port,"handbookbot","#handbook-test",False,"acct" if sasl else None,"secret" if sasl else None,required)
 def run_ok(self,mode,**kw):
  s=Fake(mode);s.start();run_session(self.cfg(s,**kw));s.join()
 def test_names_transcript_reaches_live_runtime(self):
  s=Fake("names");s.start()
  with self.assertRaises(ConnectionClosed):run_session(self.cfg(s))
  s.join()
 def test_plain_eof_is_explicit_disconnect(self):
  s=Fake("plain");s.start()
  with self.assertRaises(ConnectionClosed):run_session(self.cfg(s))
  s.join()
 def test_sasl_plain_requires_tls(self):
  c=Config("localhost",6697,"bot","#c",False,"acct","secret",True)
  with self.assertRaises(SystemExit):validate(c)
 def test_silent_server_shutdown_sends_quit(self):
  s=Fake("stop");s.start();stop=StopFlag()
  result=[]
  th=threading.Thread(target=lambda:result.append(run_session(self.cfg(s),stop)));th.start();time.sleep(.2);stop.request();th.join(2);s.join()
  self.assertFalse(th.is_alive());self.assertEqual(result,[SessionResult(False,True)])
 def test_nick_collision_then_eof_is_disconnect(self):
  s=Fake("nick");s.start()
  with self.assertRaises(ConnectionClosed):run_session(self.cfg(s))
  s.join()
 def test_server_error(self):
  s=Fake("error");s.start()
  with self.assertRaises(ServerError):run_session(self.cfg(s))
  s.join()
 def test_required_sasl_missing(self):
  s=Fake("missing");s.start()
  with self.assertRaises(AuthenticationError):run_session(self.cfg(s,required=True,sasl=True))
  s.join()
 def test_required_sasl_failure(self):
  s=Fake("fail");s.start()
  with self.assertRaises(AuthenticationError):run_session(self.cfg(s,required=True,sasl=True))
  s.join()
if __name__=="__main__":unittest.main()
