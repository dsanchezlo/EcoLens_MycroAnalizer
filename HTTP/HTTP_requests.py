from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import requests

class requestsHTTP(BaseHTTPRequestHandler):
    #GET request HTTP
    def do_GET(self):
        if self.path == "/":
            # Behandle Anfragen an den Pfad "/path2"
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # open and read the HTML file
            with open("index.html", "r") as file:
                html_content = file.read()

            self.wfile.write(bytes(html_content, "utf-8"))

        elif self.path == "/js/script.js":
            self.send_response(200)
            self.send_header("Content-type", "text/javascript")
            self.end_headers()

            # open and read the JavaScript file
            with open("js/script.js", "r") as file:
                js_content = file.read()

            self.wfile.write(bytes(js_content, "utf-8"))
        elif self.path == "/imageStreaming":
            # Behandle Anfragen an den Pfad "/path1"
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Dies ist Pfad 1.")

        else:
            # Standardverhalten für unbekannte Pfade
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Pfad nicht gefunden.")

    #POST request HTTP
    def do_POST(self):
        global urlFlash
        if self.path == "/flash":  #endpoint for the path
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            post_data = json.loads(post_data)

            #Data received in post_data
            print("Datos POST recibidos:", post_data)
            if post_data.get("mensaje") == "flashON":
                response = requests.get(urlFlash)

            self.send_response(200)
            self.end_headers()
            #self.wfile.write(b"Solicitud POST recibida exitosamente")
        else:
            print("PATH: " + self.path + " not found")

class RunServer:
    def __init__(self, host, port, flash):
        print(host)
        self.HOST = host
        self.PORT = port
        global urlFlash
        urlFlash = flash

    def run(self):
        self.server = HTTPServer((self.HOST, self.PORT), requestsHTTP)
        print("Server running...")
        self.server.serve_forever()

    def close(self):
        self.server.server_close()
        print("Server closed")
