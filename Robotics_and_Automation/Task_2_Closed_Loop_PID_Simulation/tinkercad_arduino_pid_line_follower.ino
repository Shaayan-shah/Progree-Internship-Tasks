// Progree Robotics & Automation - Task 2
// Arduino Closed-Loop PID Line Follower Controller (Tinkercad Compatible)

const int SENSOR_LEFT = A0;
const int SENSOR_RIGHT = A1;
const int MOTOR_LEFT_PWM = 5;
const int MOTOR_RIGHT_PWM = 6;
const int BASE_SPEED = 140;

float Kp = 3.2;
float Ki = 0.05;
float Kd = 1.2;

float prevError = 0.0;
float integral = 0.0;

void setup() {
  pinMode(SENSOR_LEFT, INPUT);
  pinMode(SENSOR_RIGHT, INPUT);
  pinMode(MOTOR_LEFT_PWM, OUTPUT);
  pinMode(MOTOR_RIGHT_PWM, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int valLeft = analogRead(SENSOR_LEFT);
  int valRight = analogRead(SENSOR_RIGHT);

  float error = (float)(valRight - valLeft) / 10.23;

  integral += error;
  integral = constrain(integral, -100.0, 100.0);
  float derivative = error - prevError;
  prevError = error;

  float correction = (Kp * error) + (Ki * integral) + (Kd * derivative);

  int leftMotorSpeed = constrain(BASE_SPEED + correction, 0, 255);
  int rightMotorSpeed = constrain(BASE_SPEED - correction, 0, 255);

  analogWrite(MOTOR_LEFT_PWM, leftMotorSpeed);
  analogWrite(MOTOR_RIGHT_PWM, rightMotorSpeed);
  delay(20);
}
