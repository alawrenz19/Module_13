import RoboPiLib as RPL
import time
import post_to_web as PTW
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 1
motorR = 7
sensor_R = 16
sensor_M = 17
sensor_L = 18
j = 3
i = 4.0

cool = time.time()
while time.time() < time.time + 5:
  

while RPL.digitalRead(sensor_R) and RPL.digitalRead(sensor_M) and RPL.digitalRead(sensor_L)== 1:
    PTW.state['d1'] = RPL.digitalRead(sensor_pin)
    RPL.servoWrite(motorR, 1000)
    RPL.servoWrite(motorL, 2000)
    PTW.post()
    if RPL.digitalRead(sensor_R) or RPL.digitalRead(sensor_M) or RPL.digitalRead(sensor_L) =! 1:
        break

while RPL.digitalRead(sensor_R) == 0:
    PTW.state['d1'] = RPL.digitalRead(sensor_pin)
    move = time.time()
    while time.time() < (move + i):
        RPL.servoWrite(motorR, 1490)
        RPL.servoWrite(motorL, 1520)
        PTW.post()
    while time.time() > (move + i):
        RPL.servoWrite(motorR, 1460)
        RPL.servoWrite(motorL, 1550)
        PTW.post()

while RPL.digitalRead(sensor_L) == 0:
    PTW.state['d1'] = RPL.digitalRead(sensor_pin)
    run = time.time()
    while time.time() < (run + i):
        RPL.servoWrite(motorR, 1520)
        RPL.servoWrite(motorL, 1490)
        PTW.post()
    while time.time() > (run + i):
        RPL.servoWrite(motorR, 1550)
        RPL.servoWrite(motorL, 1460)
        PTW.post()

while RPL.digitalRead(sensor_M) == 0:
    PTW.state['d1'] = RPL.digitalRead(sensor_pin)
    move = time.time()
    while time.time() < (move + i):
        RPL.servoWrite(motorR, 1490)
        RPL.servoWrite(motorL, 1520)
        PTW.post()
    while time.time() > (move + i):
        RPL.servoWrite(motorR, 1460)
        RPL.servoWrite(motorL, 1550)
        PTW.post()
