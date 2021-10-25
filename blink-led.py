from pyfirmata import Arduino, util
import time

#Realizamos conexion con el puerto del sistema operativo
#/dev/ttyUSB0 linux, COMx Windows
board = Arduino("COM7")

parpadeos= input("Cuantas veces quieres que el LED parpadee?: ")
print("El LED parpadeará " + parpadeos + " veces.")
for x in range(int(loopTimes)):
  board.digital[13].write(1)
  time.sleep(0.2)
  board.digital[13].write(0)
  time.sleep(0.2)
