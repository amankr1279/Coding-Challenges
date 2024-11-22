import http.server
from http import HTTPStatus
import socketserver
import multiprocessing
from json import dumps

class MyHTTPHandler(http.server.BaseHTTPRequestHandler):

    def log_request(self, code='-', size='-'):
        if isinstance(code, HTTPStatus):
            code = code.value
        headers = self.headers
        host = headers.get(name="Host")
        port = host.split(":")[1]
        
        self.log_message('"%s" at %s %s %s',
                         self.requestline, port, str(code), str(size))
    def do_GET(self):
        if self.path == "/":
            response = {"message": "Hello world"}
            self.send_response(200)
            
        elif self.path == "/ping":
            response = {"message": "Alive"}
            self.send_response(200)
        else:
            response = {"message": "Forbidden"}
            self.send_response(400)
        
        self.send_header("Content-type", "application/json")
        response_length = len(dumps(response))
        self.send_header("Content-Length", str(response_length))
        self.end_headers()
        self.wfile.write(str(response).encode('utf8'))

def run_webserver(PORT):
    socketserver.TCPServer.allow_reuse_address = True
    Handler = MyHTTPHandler
    http_server = http.server.HTTPServer(('localhost', PORT), Handler)
    http_server.serve_forever()

    return


if __name__ == '__main__':

    # Run servers
    servers = []
    for server_id in range(1,4): 
        p = multiprocessing.Process( target=run_webserver, args=(8080 + server_id,))
        servers.append(p)  

    for server in servers:
        server.start()

    for server in servers:
        server.join()