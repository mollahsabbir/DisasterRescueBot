# Import required modules
import time
import RPi.GPIO as GPIO
import socket

LOCALHOST = "192.168.43.203"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Server started")
print("Waiting for client request..")


# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

motorInputs = [11,12,15,16]
rightMotor = 7
leftMotor = 18
motorSpeed = GPIO.HIGH
holdingTork = GPIO.HIGH
leftMotorSpeed = motorSpeed
rightMotorSpeed = motorSpeed


# set up GPIO pins
for i in motorInputs:
    GPIO.setup(i, GPIO.OUT)

GPIO.setup(leftMotor, GPIO.OUT)
GPIO.setup(rightMotor, GPIO.OUT)


dir = 'Nothing'

def moveForward():
    # Set the motor speed
    GPIO.output(rightMotor, rightMotorSpeed)
    GPIO.output(leftMotor, leftMotorSpeed)

    # Drive the motor
    # Right Motor:
    GPIO.output(motorInputs[0], GPIO.HIGH)
    GPIO.output(motorInputs[1], GPIO.LOW)
    # Left Motor:
    GPIO.output(motorInputs[2], GPIO.HIGH)
    GPIO.output(motorInputs[3], GPIO.LOW)

def moveBackward():
    # Set the motor speed
    GPIO.output(rightMotor, rightMotorSpeed)
    GPIO.output(leftMotor, leftMotorSpeed)

    # Drive the motor
    # Right Motor:
    GPIO.output(motorInputs[0], GPIO.LOW)
    GPIO.output(motorInputs[1], GPIO.HIGH)
    # Left Motor:
    GPIO.output(motorInputs[2], GPIO.LOW)
    GPIO.output(motorInputs[3], GPIO.HIGH)

def moveLeft():
    # Set the motor speed
    GPIO.output(rightMotor, rightMotorSpeed)
    GPIO.output(leftMotor, leftMotorSpeed)

    # Drive the motor
    # Right Motor:
    GPIO.output(motorInputs[0], GPIO.HIGH)
    GPIO.output(motorInputs[1], GPIO.LOW)
    # Left Motor:
    GPIO.output(motorInputs[2], GPIO.LOW)
    GPIO.output(motorInputs[3], GPIO.LOW)

def moveRight():
    # Set the motor speed
    GPIO.output(rightMotor, rightMotorSpeed)
    GPIO.output(leftMotor, leftMotorSpeed)

    # Drive the motor
    # Right Motor:
    GPIO.output(motorInputs[0], GPIO.LOW)
    GPIO.output(motorInputs[1], GPIO.LOW)
    # Left Motor:
    GPIO.output(motorInputs[2], GPIO.HIGH)
    GPIO.output(motorInputs[3], GPIO.LOW)

def moveHardLeft():
    # Set the motor speed
    GPIO.output(rightMotor, rightMotorSpeed)
    GPIO.output(leftMotor, leftMotorSpeed)

    # Drive the motor
    # Right Motor:
    GPIO.output(motorInputs[0], GPIO.HIGH)
    GPIO.output(motorInputs[1], GPIO.LOW)
    # Left Motor:
    GPIO.output(motorInputs[2], GPIO.LOW)
    GPIO.output(motorInputs[3], GPIO.HIGH)

def moveHardRight():
    # Set the motor speed
    GPIO.output(rightMotor, rightMotorSpeed)
    GPIO.output(leftMotor, leftMotorSpeed)

    # Drive the motor
    # Right Motor:
    GPIO.output(motorInputs[0], GPIO.LOW)
    GPIO.output(motorInputs[1], GPIO.HIGH)
    # Left Motor:
    GPIO.output(motorInputs[2], GPIO.HIGH)
    GPIO.output(motorInputs[3], GPIO.LOW)

def moveStop():
    # Set the motor speed
    GPIO.output(rightMotor, rightMotorSpeed)
    GPIO.output(leftMotor, leftMotorSpeed)

    # Drive the motor
    # Right Motor:
    GPIO.output(motorInputs[0], GPIO.LOW)
    GPIO.output(motorInputs[1], GPIO.LOW)
    # Left Motor:
    GPIO.output(motorInputs[2], GPIO.LOW)
    GPIO.output(motorInputs[3], GPIO.LOW)


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