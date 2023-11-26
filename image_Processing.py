import cv2
import numpy as np
def getImage(url):
    cap = cv2.VideoCapture(url) # Crear objeto VideoCapture

    cap.open(url) # Antes de capturar el frame abrimos la url

    #The image is analised only with the specified resolution
    ret,frame = cap.read() # Captura de frame

    Conditional=True
    #Leer la referencia
    try:
        Ref=cv2.imread('Test.jpg',0)
    except:
        Conditional=False
    ###############

    if (Conditional):
        frame_proc = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        w,h = Ref.shape[::-1]
        deteccion = cv2.matchTemplate(frame_proc,Ref, cv2.TM_CCOEFF_NORMED)
        umbral = 0.7
        ubi = np.where(deteccion >= umbral)
        for pt in zip(*ubi[::-1]):
           cv2.rectangle(frame,pt,(pt[0]+w, pt[1]+h),(255,0,0),1)



        #cv2.imwrite("gespeichertes_bild.jpg", frame)
    
    if (ret):
        return cv2.imencode(".jpg", frame)
