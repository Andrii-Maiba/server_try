from http.server import HTTPServer, CGIHTTPRequestHandler
import os

class MyCGIHTTPRequestHandler(CGIHTTPRequestHandler):
    def is_cgi(self):
        # Treat .py files as CGI scripts
        if self.path.endswith('.py'):
            self.cgi_info = '', self.path[1:]  # Remove leading /
            return True
        return super().is_cgi()

server_data=('localhost', 8080)
server=HTTPServer(server_data, MyCGIHTTPRequestHandler)
server.serve_forever()
