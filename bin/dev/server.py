import http.server
import os
import signal
import socketserver
import sys

PORT = 8000

class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        '': 'application/octet-stream',
        '.manifest': 'text/cache-manifest',
        '.html': 'text/html',
        '.png': 'image/png',
        '.jpg': 'image/jpg',
        '.svg':	'image/svg+xml',
        '.css':	'text/css',
        '.js':'application/x-javascript',
        '.wasm': 'application/wasm',
        '.json': 'application/json',
        '.xml': 'application/xml',
    }

    def do_GET(self):
        if not os.path.splitext(self.path)[1]:  # Check if the path has no extension
            html_path = self.path + ".html"
            if os.path.exists(self.directory + html_path):
                print(f"Serving: {html_path}")
                self.path = html_path
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

httpd = socketserver.TCPServer(("localhost", PORT), HttpRequestHandler)

def signal_handler(sig, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    print(f"serving at http://localhost:{PORT}")
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    print("\nShutting down server...")
