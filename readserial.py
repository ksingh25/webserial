#!/usr/bin/python
#
#Simple app to read data from serial port
#It will store the data in a file. The path to the file should be provided
#Also the path to serial device may change on different systems
#Assuming that it is /dev/ttyUSB0

import serial
import os
import time
from datetime import datetime

serialdev = '/dev/ttyUSB0'

#close serial, disconnect MQTT

def cleanup():
    print("Ending and cleaning up")
    ser.close()
    file.close()

try:
   #open text file
   file = open("./sensor.txt", "a")

except:
   print("file not found")


try:
    print("Connecting... ", serialdev)
    #connect to serial port
    ser = serial.Serial(serialdev, 115200, timeout=0)
except:
    print("Failed to connect serial")
    #unable to continue with no serial input
    raise SystemExit


try:
    ser.flushInput()
    mypid = os.getpid()

    #read data from serial and write to file
    while 1:
        #print("reading..")
        file.flush()
        line = ser.readline()
        file.write(line.decode('ascii'))
        ser.flush()
 

# handle list index error (i.e. assume no data received)
except (IndexError):
    print("No data received within serial timeout period")
    cleanup()
# handle app closure
except (KeyboardInterrupt):
    print("Interrupt received")
    cleanup()
except (RuntimeError):
    print("Runtime Error!")
    cleanup()
