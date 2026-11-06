#!/usr/bin/env python3
"""Serve the static Vision website from the project root without third-party packages."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PORT = 3000


class VisionHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def send_error(self, code, message=None, explain=None):
        if code == 404:
            page = (ROOT / "404.html").read_bytes()
            self.send_response(404, "Not Found")
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(page)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(page)
            return
        super().send_error(code, message, explain)


server = ThreadingHTTPServer(("0.0.0.0", PORT), VisionHandler)
print(f"Vision local preview: http://localhost:{PORT}/")
server.serve_forever()
