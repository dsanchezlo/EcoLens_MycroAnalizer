from Webserver import Webserver
import tkinter as tk
import webbrowser
import socket

url = "http://192.168.4.1/640x480.jpg"
urlFlash="http://192.168.4.1/800x600.jpg"

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8000

server = Webserver(HOST, PORT, urlFlash, url)
#Verificar si ya se está ejecutando el servidor
serverON = False

def detener_servidor():
    global serverON
    if serverON:
        server.WSclose()
        serverON = False

def abrir_url():
    global serverON
    webbrowser.open("http://" + HOST + ":" + str(PORT))
    if not serverON:
        serverON = True
        server.WSrun()

def ejecutar():
    global serverON
    if not serverON:
        serverON = True
        server.WSrun()

def cerrar_ventana():
    detener_servidor()
    ventana.destroy()

ventana = tk.Tk()
label = tk.Label(ventana, text="Para ejecutar el microscopio debes acceder al link: " + "http://" +  HOST + ":" + str(PORT), font=("Arial", 12))
boton = tk.Button(ventana, text="Abrir URL en el navegador", command=abrir_url)
boton_detener = tk.Button(ventana, text="Detener Servidor", command=detener_servidor)
boton_ejecutar = tk.Button(ventana, text="Iniciar sin abrir link", command=ejecutar)

# Establecer el tamaño por defecto de la ventana
ventana.title("EcoLens_MycroAnalizer")
ventana.geometry("600x250")
ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)  # Intercepta el evento de cierre

label.grid(row=0, column=0, padx=10, pady=30, sticky="new")
boton.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
boton_ejecutar.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
boton_detener.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

# Configurar que la fila y la columna de la cuadrícula se expandan
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)

# Ejecutar el loop principal
ventana.mainloop()
