from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import cv2
import requests

url = "http://192.168.137.211/1024x768.jpg"
urlFlash="http://192.168.137.211/800x600.jpg"


HOST = "192.168.1.114"
#HOST = "localhost"
PORT = 8000

# Check if the url is valid
try:
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        print("The URL is accessible.")
    else:
        print(f"Failed to access the URL. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Failed to access the URL. Error: {e}")

class requestsHTTP(BaseHTTPRequestHandler):
    #GET request HTTP
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # open and read the HTML file
        with open("index.html", "r") as file:
            html_content = file.read()

        self.wfile.write(bytes(html_content, "utf-8"))

    #POST request HTTP
    def do_POST(self):
        if self.path == "/":  #endpoint for the path
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


server = HTTPServer((HOST, PORT), requestsHTTP)
print("Server running...")

server.serve_forever()
server.server_close()
print("Served closed")
