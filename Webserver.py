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

        self.server = RunServer(self.HOST, self.PORT, self.urlFlash, self.url)
        self.server.run()

    def WSclose(self):
        self.server.close()
