import RoboPiLib as RPL
import time

A = 1
sensor_1 = RPL.analogRead(0)
sensor_2 = RPL.analogRead(1)

def forward():
    RPL.servoWrite(6, 1400)
    RPL.servoWrite(7, 1600)
    print "Forward"
def stop():
    RPL.servoWrite(6, 0)
    RPL.servoWtire(7, 0)
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
    if RPL.analogRead(0) > 400:
    	move = time.time()
      	start_right()
      	while time.time() > (move + A):
            forward()
    elif RPL.analogRead(0) > 200:
    	move = time.time()
    	forward()
    	while time.time() > (move + A):
             forward()
    elif RPL.analogRead(0) - RPL.analogRead(1) > 80:
    	move = time.time()
        small_correct()
   	while time.time() > (move + A):
             forward()
    elif RPL.analogRead(1) - RPL.analogRead(0) > 80:
    	move = time.time()
        large_correct()
        while time.time() > (move + A):
             forward()
    else: 
    	move = time.time()
        start_left()
        while time.time() > (move + A):
             forward()
        
        
        
