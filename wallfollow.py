import RoboPiLib as RPL
import time

sensor_L = 24
sensor_R = 25

A = 6
        
def forward():
    RPL.servoWrite(6, 1400)
    RPL.servoWrite(7, 1600)
    
while RPL.analogRead(sensor_L) < 200:
    move = time.time()
    while time.time > (move + A):
        forward()
