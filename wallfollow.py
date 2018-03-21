import RoboPiLib as RPL
import time

A = 6
sensor_1 = RPL.analogRead(0)
sensor_2 = RPL.analogRead(1)
        
def forward():
    RPL.servoWrite(6, 1400)
    RPL.servoWrite(7, 1600)
    
while sensor_1 > 200:
    move = time.time()
    while time.time > (move + A):
        forward()
