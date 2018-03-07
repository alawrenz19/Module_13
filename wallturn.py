import RoboPiLib as RPL
import time
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 7
motorR = 6
sensor_R = 16
sensor_M = 17
sensor_L = 18
j = 3
i = 6.0

  

while RPL.digitalRead(sensor_R) and RPL.digitalRead(sensor_L)== 1:
    RPL.servoWrite(motorR, 2000)
    RPL.servoWrite(motorL, 1000)


while RPL.digitalRead(sensor_R) == 0:
    move = time.time()
    while time.time() < (move + i):
        RPL.servoWrite(motorL, 1000)
        RPL.servoWrite(motorR, 1510)
        if time.time() > (move + i):
          break

while RPL.digitalRead(sensor_L) == 0:
    run = time.time()
    while time.time() < (run + i):
        RPL.servoWrite(motorL, 1490)
        RPL.servoWrite(motorR, 2000)
        if time.time() > (move + i):
          break



