from HTTP.HTTP_requests import RunServer
import cv2
import requests

url = "http://192.168.137.226/640x480.jpg"
urlFlash="http://192.168.137.226/800x600.jpg"

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

server = RunServer(HOST, PORT, urlFlash, url)
server.run()
server.close()
