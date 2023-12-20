from http.server import BaseHTTPRequestHandler, HTTPServer
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from urllib import request
import threading
import sys


class ProxyWebSocket(WebSocket):
    def handleMessage(self):
        target_url = sys.argv[1] if len(sys.argv) > 1 else "ws://dummy.com/"
        target_ws = request.urlopen(target_url)

        target_ws.send(self.data)

        response = target_ws.recv(1024)
        self.sendMessage(response)
        return


class ProxyReqHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        target_url = sys.argv[1] if len(sys.argv) > 1 else "http://dummy.com/"
        target_res = request.urlopen(target_url)

        self.send_response(target_res.status)
        self.sendHeaders(target_res.headers)
        self.wfile.write(target_res.read())

    def sendHeaders(self, headers):
        for header, val in headers.items():
            self.send_header(header, val)
        self.end_headers()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <target_url>")
        sys.exit(1)

    http_server = HTTPServer(("localhost", 8000), ProxyReqHandler)

    websocket_server = SimpleWebSocketServer("", 9000, ProxyWebSocket)
    
    print(f"HTTP Proxy Server running at http://localhost:8000/")
    print(f"WebSocket Proxy Server running at ws://localhost:9000/")

    http_thread = threading.Thread(target=http_server.serve_forever)
    websocket_thread = threading.Thread(target=websocket_server.serveforever)

    http_thread.start()
    websocket_thread.start()
