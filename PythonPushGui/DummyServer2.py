from twisted.protocols import basic
from twisted.internet  import reactor, protocol, defer
import datetime

class WebPUSH(basic.LineReceiver):
    logTemplate = '''
      <script type="text/javascript">
         pushHandler.addLi('%s')
      </script>
    '''
    def __init__(self):
        self.gotRequest = False

    def lineReceived(self, line):
        if not self.gotRequest:
            self.startResponse()
            self.gotRequest = True

    def startResponse(self):
        self.sendLine('HTTP/1.1 200 OK')
        self.sendLine('Content-Type: text/html; charset=utf-8')
        self.sendLine('')
        f = open('index.html', 'r')
        self.transport.write( ''.join(f.read()) )
        f.close()
        self.logTime()

    def logTime(self):
        self.sendLine( self.logTemplate % datetime.datetime.now() )
        reactor.callLater(2, self.logTime)

if __name__ == '__main__':
    f = protocol.ServerFactory()
    f.protocol = WebPUSH
    reactor.listenTCP(8080, f)
    reactor.run()
  