import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

url='http://192.168.137.18/1024x768.jpg'
urlFlash='http://192.168.137.18/800x600.jpg'
cap = cv2.VideoCapture(url) # Crear objeto VideoCapture

winName = 'IP_CAM'
cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)

link = url

while(1):
    cap.open(link) # Antes de capturar el frame abrimos la url

    #The image is analised only with the specified resolution
    if link == url:
        ret,frame = cap.read() # Captura de frame
        if ret:
            #frame = cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
            gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gris, 1.1, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

            cv2.imshow(winName,frame)

    tecla = cv2.waitKey(1) & 0xFF


    if link == urlFlash:
        link = url

    #By pressing "space" the flasLED turns on
    if tecla == 32:
        link = urlFlash

    #By pressing "esc" the process ends
    if tecla == 27:
        break

cv2.destroyAllWindows()
