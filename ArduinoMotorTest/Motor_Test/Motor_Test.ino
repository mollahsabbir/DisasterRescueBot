/*
 Name:		Motor_Test.ino
 Created:	07-Feb-18 10:34:29 PM
 Author:	BLANK
*/

const int motor_inputs[4] = { 9, 10, 11, 12 };
const int leftMotor = 5;
const int rightMotor = 6;
//const int motor_driver_on = 36;

const int motorSpeed = 250;
const int holdingTork = 250;

int leftMotorSpeed = motorSpeed;
int rightMotorSpeed = motorSpeed;

int x = 1000;   // Control delay in milliseconds

char dir = 'R';   // Direction of the bot


void setup()
{
	for (int i = 0; i < 4; i++)
	{
		pinMode(motor_inputs[i], OUTPUT);
	}
	// digitalWrite(motor_driver_on, HIGH);

	pinMode(leftMotor, OUTPUT);
	pinMode(rightMotor, OUTPUT);

	Serial.begin(9600);
}

void loop()
{
	if (dir == 'W')
	{
		moveForward();
	}

	else if (dir == 'S')
	{
		moveBackward();
	}

	else if (dir == 'A')
	{
		moveLeft();
	}

	else if (dir == 'D')
	{
		moveRight();
	}

	else if (dir == 'L')
	{
		moveLEFT();
	}

	else if (dir == 'R')
	{
		moveRIGHT();
	}

	else
	{
		moveStop();
	}
}

void moveForward()
{
	analogWrite(leftMotor, motorSpeed);
	analogWrite(rightMotor, motorSpeed);
	digitalWrite(motor_inputs[0], HIGH);
	digitalWrite(motor_inputs[1], LOW);
	digitalWrite(motor_inputs[2], HIGH);
	digitalWrite(motor_inputs[3], LOW);
	Serial.println("Forward");
}

void moveBackward()
{
	analogWrite(leftMotor, motorSpeed);
	analogWrite(rightMotor, motorSpeed);
	digitalWrite(motor_inputs[0], LOW);
	digitalWrite(motor_inputs[1], HIGH);
	digitalWrite(motor_inputs[2], LOW);
	digitalWrite(motor_inputs[3], HIGH);
	Serial.println("Back");
}

void moveRight()
{
	analogWrite(leftMotor, motorSpeed);
	analogWrite(rightMotor, motorSpeed);
	digitalWrite(motor_inputs[0], LOW);
	digitalWrite(motor_inputs[1], LOW);
	digitalWrite(motor_inputs[2], HIGH);
	digitalWrite(motor_inputs[3], LOW);
	Serial.println("Right");
}

void moveLeft()
{
	analogWrite(leftMotor, motorSpeed);
	analogWrite(rightMotor, motorSpeed);
	digitalWrite(motor_inputs[0], HIGH);
	digitalWrite(motor_inputs[1], LOW);
	digitalWrite(motor_inputs[2], LOW);
	digitalWrite(motor_inputs[3], LOW);
	Serial.println("Left");
}

void moveRIGHT()
{
	analogWrite(leftMotor, motorSpeed);
	analogWrite(rightMotor, holdingTork);
	digitalWrite(motor_inputs[0], LOW);
	digitalWrite(motor_inputs[1], HIGH);
	digitalWrite(motor_inputs[2], HIGH);
	digitalWrite(motor_inputs[3], LOW);
	Serial.println("RIGHT");
}

void moveLEFT()
{
	analogWrite(leftMotor, holdingTork);
	analogWrite(rightMotor, motorSpeed);
	digitalWrite(motor_inputs[0], HIGH);
	digitalWrite(motor_inputs[1], LOW);
	digitalWrite(motor_inputs[2], LOW);
	digitalWrite(motor_inputs[3], HIGH);
	Serial.println("LEFT");
}

void moveStop()
{
	analogWrite(leftMotor, motorSpeed);
	analogWrite(rightMotor, motorSpeed);
	digitalWrite(motor_inputs[0], LOW);
	digitalWrite(motor_inputs[1], LOW);
	digitalWrite(motor_inputs[2], LOW);
	digitalWrite(motor_inputs[3], LOW);
	Serial.println("Stopped");
}
