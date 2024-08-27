import serial
from serial import *
arduino = serial.Serial(
    port='COM3',
    timeout=1
    parity=PARITY_NONE,
    stopbits=STOPBITS_ONE,
    rtscts=False,
    dsrdtr=False
)
integer = 24
new_line = '\r\n'

# arduino.write("\r\n")
arduino.write(integer.to_bytes())

arduino.write(bytes(new_line,'utf-8'))
