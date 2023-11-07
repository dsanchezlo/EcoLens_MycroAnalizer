import serial

try:
    BT=serial.Serial('COM6',9600)
    print('Conexion Exitosa')
except:
    print('Error de conexion')

while True:
    mensaje=input('Ingrese el mensaje: ')
    BT.write(mensaje.encode('utf-8'))
    print(BT.readline().decode('utf').rstrip('\n'))