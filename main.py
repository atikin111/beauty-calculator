from http.server import HTTPServer, SimpleHTTPRequestHandler


def run() -> None:
    host = "127.0.0.1"
    port = 8000
    server = HTTPServer((host, port), SimpleHTTPRequestHandler)
    print(f"Open http://{host}:{port}/index.html")
    server.serve_forever()


if __name__ == "__main__":
    run()
