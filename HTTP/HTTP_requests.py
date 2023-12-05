from http.server import HTTPServer, BaseHTTPRequestHandler
from image_Processing import getImage
import json
import requests
import threading
import os
import re

def get_connected_ssid():
    result = os.popen('netsh wlan show interfaces').read()
    matches = re.findall(r'SSID\s*:\s(.*)', result)
    if matches:
        return matches[0].strip()

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
            with open("js/script.js", "r", encoding='utf-8') as file:
                js_content = file.read()

            self.wfile.write(bytes(js_content, "utf-8"))

        elif self.path == "/css/design.css":
            self.send_response(200)
            self.send_header("Content-type", "text/css")  # Setze den Content-Type auf CSS
            self.end_headers()

            # Öffne und lese den Inhalt der CSS-Datei
            with open("css/design.css", "r") as file:
                css_content = file.read()

            self.wfile.write(bytes(css_content, "utf-8"))

        elif self.path == "images/icon-simple.ico":
            self.send_response(200)
            self.send_header("Content-type", "image/x-icon")
            self.end_headers()

            icon_path = "images/icon-simple.ico"  # Ersetzen Sie dies durch den tatsächlichen Pfad zu Ihrem Favicon
            with open(icon_path, "rb") as icon_file:
                icon_data = icon_file.read()
                self.wfile.write(icon_data)


        elif self.path == "/defaultImage":
            # Behandle Anfragen an den Pfad "/path1"
            self.send_response(200)
            self.send_header("Content-type", "image/jpeg")  # Setzen Sie den korrekten Content-Type für Ihr Bild
            self.end_headers()

            image_path = "images/Logo640x480.png"  # Ersetzen Sie dies durch den tatsächlichen Pfad zu Ihrem Bild
            with open(image_path, "rb") as image_file:
                image_error = image_file.read()
                self.wfile.write(image_error)

        elif self.path == "/imageStreaming":
            # Behandle Anfragen an den Pfad "/path1"
            self.send_response(200)
            self.send_header("Content-type", "image/png")  # Setzen Sie den korrekten Content-Type für Ihr Bild
            self.end_headers()

            ssid = get_connected_ssid()
            sequence = "EcoLensNUM"

            if sequence in ssid:
                done, image_data = getImage(url)
                if done==True:
                    self.wfile.write(image_data.tobytes())
                else:
                    image_path = "images/error.jpeg"  # Ersetzen Sie dies durch den tatsächlichen Pfad zu Ihrem Bild
                    with open(image_path, "rb") as image_file:
                        image_error = image_file.read()
                        self.wfile.write(image_error)
            else:
                image_path = "images/error.png"  # Ersetzen Sie dies durch den tatsächlichen Pfad zu Ihrem Bild
                with open(image_path, "rb") as image_file:
                    image_error = image_file.read()
                    self.wfile.write(image_error)

        else:
            # Standardverhalten für unbekannte Pfade
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Pfad nicht gefunden.")

    #POST request HTTP
    def do_POST(self):
        global urlFlash
        ssid = get_connected_ssid()
        sequence = "EcoLensNUM"

        if sequence in ssid:
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
            else:
                print("PATH: " + self.path + " not found")
        else:
            self.wfile.write(b"Error")

class RunServer:
    def __init__(self, host, port, flash, link):
        self.HOST = host
        self.PORT = port
        global urlFlash
        global url
        urlFlash = flash
        url = link

    def run(self):
        self.server = HTTPServer((self.HOST, self.PORT), requestsHTTP)
        print("Server running...")
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.start()

    def close(self):
        self.server.server_close()  # Detener el servidor
        self.server_thread.join()  # Esperar a que el hilo termine
        print("Server closed")
