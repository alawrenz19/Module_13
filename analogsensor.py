mport RoboPiLib as RPL
import time
RPL.RoboPiInit("/dev/ttyAMA0",115200)

sensor_1 = RPL.analogRead(0)

def forward():
    RPL.servoWrite(6, 1400)
    RPL.servoWrite(7, 1600)
    print "Forward"

while True: 
  if sensor_1 > 300:
    forward()

