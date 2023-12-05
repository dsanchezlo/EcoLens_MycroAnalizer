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
ventana.configure(bg="#f5f5f5")

# Pfad zum Icon-Datei (ICO-Format für Windows)
icon_path = "images/icon-simple.ico"

try:
    ventana.iconbitmap(icon_path)
except tk.TclError:
    print(f"Warnung: Konnte das Icon nicht laden. Überprüfe den Pfad: {icon_path}")

label = tk.Label(ventana, text="\nSi quieres usar otro dispositivo para \nver la imagen, presiona el botón\n\"Iniciar sin abrir link\" y escribe\n\n" + "http://" +  HOST + ":" + str(PORT) + "\n\nen el navegador que desees :)" + "\n\n\n\nRecuerda que debes conectarte a la red\nde tu Ecolens Microanalyzer para poder ver\ncorrectamente la imagen", font=("Verdana", 12))
boton = tk.Button(ventana, text="Abrir URL en el navegador", command=abrir_url, bg="#052f5c", fg="white", font=("Verdana", 12, "bold"), height=2)  # fg setzt die Textfarbe
boton_detener = tk.Button(ventana, text="Detener Servidor", command=detener_servidor, bg="#052f5c", fg="white", font=("Verdana", 12, "bold"), height=2)
boton_ejecutar = tk.Button(ventana, text="Iniciar sin abrir link", command=ejecutar, bg="#052f5c", fg="white", font=("Verdana", 12, "bold"), height=2)


# Establecer el tamaño por defecto de la ventana
ventana.title("EcoLens MycroAnalizer")
ventana.geometry("400x505")
ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)  # Intercepta el evento de cierre

label.grid(row=0, column=0, padx=10, pady=20, sticky="new")
boton.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
boton_ejecutar.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
boton_detener.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

# Configurar que la fila y la columna de la cuadrícula se expandan
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)

# Ejecutar el loop principal
ventana.mainloop()
