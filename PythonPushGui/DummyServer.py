from threading import Thread
from SocketServer import ThreadingMixIn
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write("<addressbook><person><name>Eric Idle</name><phone type='fix'>999-999-999</phone><phone type='mobile'>555-555-555</phone><address><street>12, spam road</street><city>London</city><zip>H4B 1X3</zip></address></person><person><name>Terry Gilliam</name><phone type='mobile'>555-555-554</phone><phone type='fix'>999-999-998</phone><address><street>3, Brazil Lane</street><city>Leeds</city><zip>F2A 2S5</zip></address></person></addressbook>")

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass

def serve_on_port(port):
    server = ThreadingHTTPServer(("localhost",port), Handler)
    server.serve_forever()

Thread(target=serve_on_port, args=[1111]).start()
serve_on_port(2222)
