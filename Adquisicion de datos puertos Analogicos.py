from pyfirmata import Arduino, util
import time

#Realizamos conexion con el puerto del sistema operativo
#/dev/ttyUSB0 linux, COMx Windows
board = Arduino("COM3")

iterator = util.Iterator(board)
iterator.start()
board.analog[0].enable_reporting()

while True:
	val = board.analog[0].read()
	print ("lectura : %s" % val)
	time.sleep(1)