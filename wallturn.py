import RoboPiLib as RPL
import time
import post_to_web as PTW
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 7
motorR = 6
sensor_R = 16
sensor_M = 17
sensor_L = 18
j = 3
i = 4.0

  

while RPL.digitalRead(sensor_R) and RPL.digitalRead(sensor_M) and RPL.digitalRead(sensor_L)== 1:
    RPL.servoWrite(motorR, 2000)
    RPL.servoWrite(motorL, 1000)


while RPL.digitalRead(sensor_R) == 0:
    move = time.time()
    while time.time() < (move + j):
        RPL.servoWrite(motorL, 1000)
        RPL.servoWrite(motorR, 1510)
    while time.time() > (move + i):
        RPL.servoWrite(motorL, 1460)
        RPL.servoWrite(motorR, 1550)

while RPL.digitalRead(sensor_L) == 0:
    run = time.time()
    while time.time() < (run + j):
        RPL.servoWrite(motorL, 1490)
        RPL.servoWrite(motorR, 2000)

    while time.time() > (run + i):
        RPL.servoWrite(motorL, 1460)
        RPL.servoWrite(motorR, 1540)

while RPL.digitalRead(sensor_M) == 0:
    move = time.time()
    while time.time() < (move + j):
        RPL.servoWrite(motorL, 1000)
        RPL.servoWrite(motorR, 1510)
    while time.time() > (move + i):
        RPL.servoWrite(motorL, 1460)
        RPL.servoWrite(motorR, 1550)

