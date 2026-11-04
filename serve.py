import http.server
import socketserver


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        super().end_headers()


if __name__ == "__main__":
    with socketserver.TCPServer(("", 8000), NoCacheHandler) as httpd:
        print("Serving on http://localhost:8000 (no-cache)")
        httpd.serve_forever()
