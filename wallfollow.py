import RoboPiLib as RPL
import time

A = 6
        
def forward():
    RPL.servoWrite(6, 1400)
    RPL.servoWrite(7, 1600)
    
while RPL.analogRead(25) and RPL.analogRead(24) > 200:
    move = time.time()
    while time.time > (move + A):
        forward()
