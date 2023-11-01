import cv2

def getImage(url):
    cap = cv2.VideoCapture(url) # Crear objeto VideoCapture

    cap.open(url) # Antes de capturar el frame abrimos la url

    #The image is analised only with the specified resolution
    ret,frame = cap.read() # Captura de frame

    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imwrite("gespeichertes_bild.jpg", frame)
        return cv2.imencode(".jpg", frame)
