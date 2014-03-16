import wx
import urllib2
import ConnectStrings
import GetClientIdHandler
import StatusManager
import AddToStreamHandler
import XmlProcess
import PushServer
from twisted.protocols import basic
from twisted.internet  import reactor, protocol, defer
import datetime

from xml.sax import make_parser,SAXException

f = PushServer.protocol.ServerFactory()
f.protocol =PushServer.WebPUSH
reactor.listenTCP(8081, f)
reactor.run()

#req_GetClientId = ConnectStrings.GetString_ServerHeader()+'?'+ConnectStrings.GetString_GetClientId()
#print req_GetClientId
#
#getClientIdHandler=GetClientIdHandler.GetClientIdHandler()
#parser=make_parser()
#parser.setContentHandler(getClientIdHandler)
#parser.parse(req_GetClientId)
#print StatusManager.StatusManager.clientId
#
#req_AddStream=ConnectStrings.GetString_ServerHeader()+'?'+ConnectStrings.GetString_AddToStream()
#print req_AddStream
#addToStreamHandler=AddToStreamHandler.AddToStreamHandler()
#parser2=make_parser()
#parser2.setContentHandler(addToStreamHandler)
#
#url=req_AddStream
#StatusManager.StatusManager.stream=urllib2.urlopen(url)
#tagList=[]
#str=''
#while 1:
#    char=StatusManager.StatusManager.stream.read(1)
#    if char=='<':
#        nextChar=StatusManager.StatusManager.stream.read(1)
#        while nextChar!='>':
#            str+=nextChar
#            nextChar=StatusManager.StatusManager.stream.read(1)
#        XmlProcess.ProcessNode(str)
#        str=''
