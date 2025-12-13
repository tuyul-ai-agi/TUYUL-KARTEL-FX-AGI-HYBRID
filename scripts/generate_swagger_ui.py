# ============================================================
# 🧠 TUYUL FX AGI v5.7.8 – Swagger Reflective Server
# ============================================================

import http.server
import os
import socketserver

PORT = 9000
os.chdir("docs")


def main():
    print(
        "🌐 Starting Swagger UI for TUYUL FX AGI Reflective API " f"on port {PORT}"
    )
    handler = http.server.SimpleHTTPRequestHandler
    socketserver.TCPServer(("", PORT), handler).serve_forever()


if __name__ == "__main__":
    main()
