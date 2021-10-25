import serial,sys

#Realizamos conexion con el puerto del sistema operativo
#/dev/ttyUSB0 linux, COMx Windows
ser=serial.Serial('/dev/ttyUSB0',9600, timeout=None)

ser.flushInput()

char = raw_input("Enter String : ")
ser.write(char)

received =[]

for n in range(0, len(char)):
     char_rec = ser.readline()
     received.append(char_rec[0:len(char_rec)-2]) # remove \r\n characters

sys.stdout.write(''.join(received)+'\n')
ser.close()
