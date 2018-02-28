import RoboPiLib as RPL
from setup import RPL
import post_to_web as PTW
RPL.RoboPiInit("/dev/ttyAMA0",115200)

print "Please type in the speed you want your motors to be at:"
NumberL = int(raw_input("Left Motor > "))
NumberR = int(raw_input("Right Motor > "))

RPL.servoWrite(6, NumberR)
RPL.servoWrite(7, NumberL)

