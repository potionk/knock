import json
from http.server import BaseHTTPRequestHandler, HTTPServer

port = 8282


class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "healthy"}).encode())
        else:
            self.send_error(404, 'Not Found')


def run_server():
    server_address = ('', port)
    httpd = HTTPServer(server_address, HealthCheckHandler)
    print(f'Server running on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
