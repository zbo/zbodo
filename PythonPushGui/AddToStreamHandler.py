import StatusManager
from xml.sax import make_parser,SAXException
from xml.sax.handler import ContentHandler

class AddToStreamHandler(ContentHandler):
    def new(self):
        return
    def __init__(self):
        return
    def startElement(self,name,attrs):
        print name
    def endElement(self,name):
        print name
        return
    def characters(self,chars):
        print chars
        return