import RoboPiLib as RPL
import time
RPL.RoboPiInit("/dev/ttyAMA0",115200)

sensor_1 = RPL.analogRead(0)
sensor_2 = RPL.analogRead(1)

def forward():
    RPL.servoWrite(6, 1400)
    RPL.servoWrite(7, 1600)
    print "Forward"
def stop():
    RPL.servoWrite(6, 0)
    RPL.servoWrite(7, 0)
    print "stop"
def start_right():
    RPL.servoWrite(7, 1550)
    RPL.servoWrite(6, 1420)
    print "Turning Right"
def start_left():
    RPL.servoWrite(6, 1460)
    RPL.servoWrite(7, 1550)
    print "Turning Left"
def small_correct():
    RPL.servoWrite(7, 1550)
    RPL.servoWrite(6, 1420)
    print "RIGHT correction"
def large_correct():
    RPL.servoWrite(6, 1460)
    RPL.servoWrite(7, 1570)
    print "LEFT correction"
    
while True: 
    sensor_1 = RPL.analogRead(0)
    sensor_2 = RPL.analogRead(1)
    
    if sensor_1 or sensor_2 > 100:
      	start_right()
    
    if sensor_1 and sensor_2 < 100 , sensor_1 and sensor_2 > 50
        forward()
    
    if sensor_1 or sensor_2 < 50
        start_left()
        
        
        
