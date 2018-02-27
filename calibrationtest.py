import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

while True:
    RPL.servoWrite(0, raw_input("> "))
    RPL.servoWrite(0, raw_input("> "))
    
