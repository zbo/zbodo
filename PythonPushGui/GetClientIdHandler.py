import StatusManager
from xml.sax import make_parser,SAXException
from xml.sax.handler import ContentHandler

class GetClientIdHandler(ContentHandler):
    def new(self):
        return
    def __init__(self):
        return
    def startElement(self,name,attrs):
        StatusManager.StatusManager.clientId=attrs._attrs['clientID']
    def endElement(self,name):
        return
    def characters(self,chars):
        print chars
        return