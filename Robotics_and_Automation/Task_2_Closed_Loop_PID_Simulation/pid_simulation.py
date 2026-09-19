# Progree Robotics & Automation — Task 2
# Beginner-Friendly Closed-Loop PID Line Follower Simulation

import time
import numpy as np

class PIDController:
    def __init__(self, Kp=3.5, Ki=1.2, Kd=0.6, setpoint=0.0):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.prev_error = 0.0
        self.integral = 0.0

    def compute(self, current_position, dt=0.02):
        # 1. Calculate tracking error
        error = self.setpoint - current_position
        
        # 2. Accumulate integral (with anti-windup clamp)
        self.integral += error * dt
        self.integral = max(-10.0, min(10.0, self.integral))
        
        # 3. Calculate derivative
        derivative = (error - self.prev_error) / dt if dt > 0 else 0.0
        self.prev_error = error
        
        # 4. Total PID control output
        output = (self.Kp * error) + (self.Ki * self.integral) + (self.Kd * derivative)
        return output, error

def run_simulation():
    pid = PIDController(Kp=4.0, Ki=0.5, Kd=1.2, setpoint=0.0)
    pos = 5.0  # Initial robot displacement (5.0 cm off-center)
    dt = 0.02
    for step in range(150):
        control_steering, error = pid.compute(pos, dt)
        pos += (control_steering * 0.25) * dt
    print(f"PID Simulation completed. Settled Position: {pos:.4f} cm (Target: 0.0 cm)")

if __name__ == "__main__":
    run_simulation()
