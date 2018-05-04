import RoboPiLib as RPL
import time
import post_to_web as PTW
RPL.RoboPiInit("/dev/ttyAMA0",115200)

i = 3

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
    move_forward = False 
    move_left = False
    move_right = False
    stop = False
    right = False
    left = False
    
    if sensor_1 > 400:
        move_right = True
    elif sensor_1 > 50:
        move_forward = True
    elif sensor_1 - sensor_2 > 80:
        right = True
    elif sensor_2 - sensor_1 > 80:
        left = True
    else: 
        move_left = True

     
   
    if move_forward:
        forward()
    elif stop:
        stop()
    elif move_left:
        start_left()
    elif move_right:
        start_right()
    elif right:
        small_correct()
    elif left:
        large_correct()

        
        
