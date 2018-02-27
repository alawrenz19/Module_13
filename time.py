import RoboPiLib as RPL
from setup import RPL
import time
import post_to_web as PTW
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 1
motorR = 0
t_ime = time.time()
i = 3
e = 6

while True:
    while time.time() < t_ime + i:
        RPL.servoWrite(motorR, 1000)
        RPL.servoWrite(motorL, 2000)
    while time.time() > t_ime + i and time.time() < t_ime + e:
        RPL.servoWrite(motorR, 0)
        RPL.servoWrite(motorL, 0)
    while time.time() > t_ime + e:
        i = i + 3
        e = e + 3
