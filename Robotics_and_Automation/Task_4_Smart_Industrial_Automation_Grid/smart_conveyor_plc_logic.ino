// Progree Robotics & Automation - Task 4
// Smart Conveyor PLC Logic & Edge Telemetry Controller

#include <Servo.h>

const int TRIG_PIN = 7;
const int ECHO_PIN = 8;
const int PROXIMITY_PIN = 2;
const int CONVEYOR_MOTOR_PWM = 9;
const int SERVO_GATE_PIN = 10;
const int LED_STATUS_OK = 11;
const int LED_FAILSAFE = 12;

Servo sortGate;

void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(PROXIMITY_PIN, INPUT_PULLUP);
  pinMode(CONVEYOR_MOTOR_PWM, OUTPUT);
  pinMode(LED_STATUS_OK, OUTPUT);
  pinMode(LED_FAILSAFE, OUTPUT);
  
  sortGate.attach(SERVO_GATE_PIN);
  sortGate.write(0);
  Serial.begin(115200);
}

long measureDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  long duration = pulseIn(ECHO_PIN, HIGH, 25000);
  return (duration == 0) ? 999 : (duration * 0.034 / 2);
}

void loop() {
  long distance = measureDistance();
  bool objectDetected = (distance > 2 && distance < 15);
  bool isMetal = (digitalRead(PROXIMITY_PIN) == LOW);

  if (objectDetected) {
    digitalWrite(LED_STATUS_OK, HIGH);
    digitalWrite(LED_FAILSAFE, LOW);
    analogWrite(CONVEYOR_MOTOR_PWM, 180);

    if (isMetal) {
      sortGate.write(60);
      Serial.println("{\"part\": \"METAL_PART\", \"action\": \"DIVERTER_A\"}");
    } else {
      sortGate.write(0);
      Serial.println("{\"part\": \"PLASTIC_PART\", \"action\": \"STANDARD_LINE\"}");
    }
    delay(1500);
    sortGate.write(0);
  } else if (distance < 2) {
    analogWrite(CONVEYOR_MOTOR_PWM, 0);
    digitalWrite(LED_STATUS_OK, LOW);
    digitalWrite(LED_FAILSAFE, HIGH);
    Serial.println("{\"part\": \"JAM_ERROR\", \"action\": \"EMERGENCY_STOP\"}");
    delay(1000);
  } else {
    analogWrite(CONVEYOR_MOTOR_PWM, 140);
  }
  delay(100);
}
