#Team Members: Hansini Ramachandran and Satwika Vemuri
#Github Repo:

import time
import grovepi

# Connect the Grove Temperature Sensor to analog port A0
# SIG,NC,VCC,GND
sensor = 0

while True:
    try:
        temp = grovepi.temp(sensor,'1.1') #change this version number possibly
        print("Indoor Temperature =", temp)
        time.sleep(.5)

    except KeyboardInterrupt:
        break
    except IOError:
        print ("Error")
