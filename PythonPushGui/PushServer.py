from twisted.protocols import basic
from twisted.internet  import reactor, protocol, defer
from xml.sax import make_parser,SAXException
import datetime
import StatusManager
import wx
import urllib2
import ConnectStrings
import GetClientIdHandler
import StatusManager
import AddToStreamHandler
import XmlProcess
import threading
import TestCode

class WebPUSH(basic.LineReceiver):
    logTemplate = '''
      <script type="text/javascript">
         pushHandler.addLi('%s')
      </script>
    '''
    processTemplate='''
        <script type="text/javascript">
            pushHandler.process('%s')
        </script>
    '''
    def StartWork(self):
        StatusManager.StatusManager.pushServer=self
        req_GetClientId = ConnectStrings.GetString_ServerHeader()+'?'+ConnectStrings.GetString_GetClientId()
        print req_GetClientId

        getClientIdHandler=GetClientIdHandler.GetClientIdHandler()
        parser=make_parser()
        parser.setContentHandler(getClientIdHandler)
        parser.parse(req_GetClientId)
        print StatusManager.StatusManager.clientId

        req_AddStream=ConnectStrings.GetString_ServerHeader()+'?'+ConnectStrings.GetString_AddToStream()
        print req_AddStream
        addToStreamHandler=AddToStreamHandler.AddToStreamHandler()
        parser2=make_parser()
        parser2.setContentHandler(addToStreamHandler)

        url=req_AddStream
        StatusManager.StatusManager.stream=urllib2.urlopen(url)
        tagList=[]
        str=''
        while 1:
            char=StatusManager.StatusManager.stream.read(1)
            if char=='<':
                nextChar=StatusManager.StatusManager.stream.read(1)
                while nextChar!='>':
                    str+=nextChar
                    nextChar=StatusManager.StatusManager.stream.read(1)
                XmlProcess.ProcessNode(str)
                str=''


    def __init__(self):
        self.gotRequest = False

    def lineReceived(self, line):
        attributes=line.split(' ')
        print attributes
        if attributes[0]!='GET':
            return
        else:
            if self.gotRequest:
                return
            queryString=attributes[1]
            if queryString=='/':
                #self.getPage()
                self.startResponse()
                self.gotRequest = True
            elif queryString[0:12]=='/addResource':
                queryArray=queryString.split('=')
                resourceName=queryArray[1]
                workThread = threading.Thread(target=XmlProcess.AddResource,args=(resourceName,))
                workThread.start()
                #XmlProcess.AddResource(resourceName)
            elif queryString=='/sendTR':
                workThread = threading.Thread(target=XmlProcess.SendTR)
                workThread.start()
            elif queryString=='/stream':
                self.startResponse()
                self.gotRequest = True

    def rawDataReceived(self, data):
        print data
        
    def getPage(self):
        self.sendLine('HTTP/1.1 200 OK')
        self.sendLine('Content-Type: text/html; charset=utf-8')
        self.sendLine('')
        f = open('index.html', 'r')
        self.transport.write( ''.join(f.read()) )
        f.close()
        self.transport.write("221 Goodbye\n")
        self.transport.loseConnection()

    def addJquery(self):
        self.sendLine('<script type="text/javascript">')
        f = open('jquery.min.js', 'r')
        self.transport.write( ''.join(f.read()) )
        f.close()
        self.sendLine('</script>')
        
    def startResponse(self):
        self.sendLine('HTTP/1.1 200 OK')
        self.sendLine('Content-Type: text/html; charset=utf-8')
        self.sendLine('')
        self.addJquery()
        f = open('index.html', 'r')
        self.transport.write( ''.join(f.read()) )
        f.close()
        StatusManager.StatusManager.connected=True
        workThread = threading.Thread(target=self.StartWork)
        workThread.start()
        print self
        self.Push()

    def PushReactor(self,str):
        reactor.callLater(0.02, self.PushContent,str)

    def PushContent(self,str):
        self.sendLine( self.logTemplate % str )

    def Push(self):
        content=StatusManager.StatusManager().GetNextPush()
        if content!=None:
            #self.sendLine( self.logTemplate % content )
            self.sendLine( self.processTemplate % content )
        reactor.callLater(0.02, self.Push)

if __name__ == '__main__':
    f = protocol.ServerFactory()
    f.protocol = WebPUSH
    reactor.listenTCP(8081, f)
    reactor.run()
  