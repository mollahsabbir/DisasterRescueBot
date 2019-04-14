from pyfirmata import Arduino, util
from pyfirmata import INPUT, OUTPUT, PWM

board = Arduino('/dev/ttyACM0')

motorInputs = [9,10,11,12]
leftMotor = 5
rightMotor = 6

motorSpeed = 0.95
holdingTork = 0.95

leftMotorSpeed = motorSpeed
rightMotorSpeed = motorSpeed

for i in motorInputs:
    board.digital[i].mode = OUTPUT

board.digital[rightMotor].mode = PWM
board.digital[leftMotor].mode = PWM

dir = 'A'

def moveForward():
    board.digital[leftMotor].write(motorSpeed)
    board.digital[rightMotor].write(motorSpeed)
    board.digital[motorInputs[0]].write(1)
    board.digital[motorInputs[1]].write(0)
    board.digital[motorInputs[2]].write(1)
    board.digital[motorInputs[3]].write(0)

def moveBackward():
    board.digital[leftMotor].write(motorSpeed)
    board.digital[rightMotor].write(motorSpeed)
    board.digital[motorInputs[0]].write(0)
    board.digital[motorInputs[1]].write(1)
    board.digital[motorInputs[2]].write(0)
    board.digital[motorInputs[3]].write(1)

def moveLeft():
    board.digital[leftMotor].write(motorSpeed)
    board.digital[rightMotor].write(motorSpeed)
    board.digital[motorInputs[0]].write(1)
    board.digital[motorInputs[1]].write(0)
    board.digital[motorInputs[2]].write(0)
    board.digital[motorInputs[3]].write(0)

def moveRight():
    board.digital[leftMotor].write(motorSpeed)
    board.digital[rightMotor].write(motorSpeed)
    board.digital[motorInputs[0]].write(0)
    board.digital[motorInputs[1]].write(0)
    board.digital[motorInputs[2]].write(1)
    board.digital[motorInputs[3]].write(0)

def moveHardLeft():
    board.digital[leftMotor].write(motorSpeed)
    board.digital[rightMotor].write(motorSpeed)
    board.digital[motorInputs[0]].write(1)
    board.digital[motorInputs[1]].write(0)
    board.digital[motorInputs[2]].write(0)
    board.digital[motorInputs[3]].write(1)

def moveHardRight():
    board.digital[leftMotor].write(motorSpeed)
    board.digital[rightMotor].write(motorSpeed)
    board.digital[motorInputs[0]].write(0)
    board.digital[motorInputs[1]].write(1)
    board.digital[motorInputs[2]].write(1)
    board.digital[motorInputs[3]].write(0)

def moveStop():
    board.digital[leftMotor].write(motorSpeed)
    board.digital[rightMotor].write(motorSpeed)
    board.digital[motorInputs[0]].write(0)
    board.digital[motorInputs[1]].write(0)
    board.digital[motorInputs[2]].write(0)
    board.digital[motorInputs[3]].write(0)

while True:
    if dir == 'W':
	    moveForward()
    elif dir == 'S':
	    moveBackward()
    elif dir == 'A':
	    moveLeft()
    elif dir == 'D':
        moveRight()
    elif dir == 'L':
        moveHardLeft()
    elif dir == 'R':
        moveHardRight()
    else:
        moveStop()


