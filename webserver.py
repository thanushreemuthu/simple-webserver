from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")

        # Read content from file.html
        try:
            with open("index.html", "r", encoding="utf-8") as file:
                content = file.read()
        except FileNotFoundError:
            content = "<h1>404 Not Found</h1><p>File not found</p>"

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Send the response
        self.wfile.write(content.encode())

# Create server address
server_address = ('127.0.0.1', 8000)

# Listen on the specified port
httpd = HTTPServer(server_address, MyHandler)
print("MY WEBSERVER IS RUNNING ON http://127.0.0.1:8000/")
httpd.serve_forever()
