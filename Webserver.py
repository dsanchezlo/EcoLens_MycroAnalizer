from HTTP.HTTP_requests import RunServer
import cv2
import requests

class Webserver:
    def __init__(self, host, port, flash, link):
        self.HOST = host
        self.PORT = port
        self.urlFlash = flash
        self.url = link

    def WSrun(self):
        # Check if the url is valid
        try:
            response = requests.get(self.url)
            print(response)
            if response.status_code == 200:
                print("The URL is accessible.")
            else:
                print(f"Failed to access the URL. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to access the URL. Error: {e}")

        self.server = RunServer(self.HOST, self.PORT, self.urlFlash, self.url)
        self.server.run()

    def WSclose(self):
        self.server.close()
