import ConnectStrings
import urllib2
import StatusManager
from twisted.internet  import reactor, protocol, defer
global g_mutex
def AddResource(resource):
    req_AddResource = ConnectStrings.GetString_ServerHeader()+'?'+ConnectStrings.GetString_AddResource(resource)
    print req_AddResource
    url=req_AddResource
    stream2=urllib2.urlopen(url)
    str=''
    str2=''
    while 1:
        str2+= stream2.read(1)
        if len(str2)>0:
            str+=str2
            str2=''
        else:
            print str
            return
def SendTR():
    req_SendTr = ConnectStrings.GetString_ServerHeader()+'?'+ConnectStrings.GetString_SendTR()
    print req_SendTr
    url=req_SendTr
    stream2=urllib2.urlopen(url)
    str=''
    str2=''
    while 1:
        str2+= stream2.read(1)
        if len(str2)>0:
            str+=str2
            str2=''
        else:
            print str
            return

def ProcessER(attrs):
    for i in range(1, len(attrs)):
        #print attrs[i]
        attrName=attrs[i].split('=')[0]
        attrValue=attrs[i].split('=')[1]
        if attrName=='resourceID':
            length=len(attrValue)
            AddResource(attrValue[1:length-1])

def ProcessSD(node):
    print node
    StatusManager.StatusManager.pushContentQueue.put(node)
    return


def ProcessWindowDisplay(node):
    StatusManager.StatusManager.pushContentQueue.put(node)
    print node

def ProcessBC(node):
    StatusManager.StatusManager.pushContentQueue.put(node)
    print node

def ProcessCD(node):
    StatusManager.StatusManager.pushContentQueue.put(node)
    print node

def ProcessAddCell(node):
    StatusManager.StatusManager.pushContentQueue.put(node)
    print node

def ProcessTR(node):
    StatusManager.StatusManager.pushContentQueue.put(node)
    print node

def ProcessHeader(header):
    StatusManager.StatusManager.pushContentQueue.put(header)
    print 'header:'+header

def ProcessEndTag(ender):
    StatusManager.StatusManager.pushContentQueue.put(ender)
    print 'endtag:'+ender

def ProcessStartTag(node,close):
    #print 'start:'+node
    attrs=node.split(' ')
    #print attrs
    name=attrs[0]
    if name=='ER':
        ProcessER(attrs)
    elif name=='SD':
        ProcessSD(node)
    elif name=='WindowDisplay':
        ProcessWindowDisplay(node)
    elif name=='BC':
        ProcessBC(node)
    elif name=='CD':
        ProcessCD(node)
    elif name=='AddCell':
        ProcessAddCell(node)
    elif name=='TR':
        ProcessTR(node)

def ProcessNode(str):
    length=len(str)
    if str=='':
        return
    elif str[0]=='?':
        ProcessHeader(str[1:length-2])
    elif str[0]=='/':
        ProcessEndTag(str[1:length])
    else:
        if str[length-1]=='/':
            str=str[0:length-2]
            ProcessStartTag(str,True)
        else:
            ProcessStartTag(str,False)
    return str

  