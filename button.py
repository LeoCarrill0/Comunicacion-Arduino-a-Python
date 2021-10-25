from pyfirmata import Arduino,util
import time

#Realizamos conexion con el puerto del sistema operativo
#/dev/ttyUSB0 linux, COMx Windows
board = Arduino("COM3")

button = board.get_pin('d:12:i')

it = util.Iterator(board)
it.start()

button.enable_reporting()

while True:
    if str(button.read()) == 'True':
        print ("Activado!")
        board.digital[13].write(1)
    else:
    	print ("Desactivado!")
    	board.digital[13].write(0)
    time.sleep(0.2)