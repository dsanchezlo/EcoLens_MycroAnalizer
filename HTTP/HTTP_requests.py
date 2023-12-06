from http.server import HTTPServer, BaseHTTPRequestHandler
#from image_Processing import getImage
import json
import requests
import threading

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
            print("hi")

        elif self.path == "/js/script.js":
            self.send_response(200)
            self.send_header("Content-type", "text/javascript")
            self.end_headers()

            # open and read the JavaScript file
            with open("js/script.js", "r", encoding='utf-8') as file:
                js_content = file.read()

            self.wfile.write(bytes(js_content, "utf-8"))

        elif self.path == "/env.json":
            self.send_response(200)
            self.send_header("Content-type", "text/json")
            self.end_headers()

            # open and read the JavaScript file
            with open("js/env.json", "r", encoding='utf-8') as file:
                js_content = file.read()

            self.wfile.write(bytes(js_content, "utf-8"))
        
        elif self.path == "/icon.png":
            self.send_response(200)
            self.send_header("Content-type", "image/png")  # Setzen Sie den korrekten Content-Type für Ihr Bild
            self.end_headers()

            image_path = "images/icon.png"  # Ersetzen Sie dies durch den tatsächlichen Pfad zu Ihrem Bild
            with open(image_path, "rb") as image_file:
                image_error = image_file.read()
                self.wfile.write(image_error)

        elif self.path == "/css/style.css":
            self.send_response(200)
            self.send_header("Content-type", "text/css")  # Setze den Content-Type auf CSS
            self.end_headers()

            # Öffne und lese den Inhalt der CSS-Datei
            with open("css/style.css", "r") as file:
                css_content = file.read()

            self.wfile.write(bytes(css_content, "utf-8"))

        # elif self.path == "/imageStreaming":
        #     # Behandle Anfragen an den Pfad "/path1"
        #     self.send_response(200)
        #     self.send_header("Content-type", "image/jpeg")  # Setzen Sie den korrekten Content-Type für Ihr Bild
        #     self.end_headers()
        #     # get image from camera
        #     done, image_data = getImage(url) 
        #     # process IA
        #     # return with text
        #     if done==True:
        #         self.wfile.write(image_data.tobytes())
        #     else:
        #         image_path = "images/error.jpg"  # Ersetzen Sie dies durch den tatsächlichen Pfad zu Ihrem Bild
        #         with open(image_path, "rb") as image_file:
        #             image_error = image_file.read()
        #             self.wfile.write(image_error)

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
