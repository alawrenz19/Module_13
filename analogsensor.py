import RoboPiLib as RPL
import time
RPL.RoboPiInit("/dev/ttyAMA0",115200)

sensor_2 = RPL.analogRead(1)

def forward():
    RPL.servoWrite(6, 1400)
    RPL.servoWrite(7, 1600)
    print "Forward"

while True: 
  if sensor_1 > 300:
    forward()

