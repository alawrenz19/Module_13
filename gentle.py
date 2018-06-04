import RoboPiLib as RPL
from setup import RPL
import time
import post_to_web as PTW
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 2
motorR = 1
sensor_pin = 17
j = 3
i = 5.

while RPL.digitalRead(sensor_pin) == 1:
    PTW.state['d1'] = RPL.digitalRead(sensor_pin)
    RPL.servoWrite(motorR, 1000)
    RPL.servoWrite(motorL, 2000)
    PTW.post()
    if RPL.digitalRead(sensor_pin) != 1:
        break

while RPL.digitalRead(sensor_pin) == 0:
    PTW.state['d1'] = RPL.digitalRead(sensor_pin)
    PTW.post()
    move = time.time()
    while time.time() < (move + i):
        RPL.servoWrite(motorR, 1475)
        RPL.servoWrite(motorL, 1520)
    while time.time() > (move + i):
        RPL.servoWrite(motorR, 0)
        RPL.servoWrite(motorL, 0)
