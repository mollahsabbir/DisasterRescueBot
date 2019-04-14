from pyfirmata import Arduino, util
from pyfirmata import INPUT, OUTPUT, PWM

import socket

LOCALHOST = "192.168.43.203"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Server started")
print("Waiting for client request..")


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

dir = 'Nothing'

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
    clientConnection,clientAddress = server.accept()
    print("Connected client :" , clientAddress)
    data = clientConnection.recv(1024)
    dir = data.decode()
    
    clientConnection.send(bytes("Successfully Connected to Server!!",'UTF-8'))
    print("Button Pressed:", dir)

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

    clientConnection.close()