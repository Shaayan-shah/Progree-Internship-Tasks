# Progree Robotics & Automation — Task 3
# Beginner 3-DOF Robotic Arm Kinematics Calculator (Forward & Inverse)

import math

class RoboticArm3DOF:
    def __init__(self, L1=10.0, L2=8.0, L3=5.0):
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3

    def forward_kinematics(self, theta1_deg, theta2_deg, theta3_deg):
        t1 = math.radians(theta1_deg)
        t2 = math.radians(theta2_deg)
        t3 = math.radians(theta3_deg)

        x = self.L1 * math.cos(t1) + self.L2 * math.cos(t1 + t2) + self.L3 * math.cos(t1 + t2 + t3)
        y = self.L1 * math.sin(t1) + self.L2 * math.sin(t1 + t2) + self.L3 * math.sin(t1 + t2 + t3)
        phi = theta1_deg + theta2_deg + theta3_deg
        return round(x, 2), round(y, 2), round(phi, 2)

    def inverse_kinematics(self, target_x, target_y, phi_deg=0.0):
        phi = math.radians(phi_deg)
        wx = target_x - self.L3 * math.cos(phi)
        wy = target_y - self.L3 * math.sin(phi)

        D = (wx**2 + wy**2 - self.L1**2 - self.L2**2) / (2 * self.L1 * self.L2)
        if abs(D) > 1.0:
            return None

        theta2_rad = math.atan2(math.sqrt(1 - D**2), D)
        theta1_rad = math.atan2(wy, wx) - math.atan2(self.L2 * math.sin(theta2_rad), self.L1 + self.L2 * math.cos(theta2_rad))
        theta3_rad = phi - (theta1_rad + theta2_rad)

        return (
            round(math.degrees(theta1_rad), 2),
            round(math.degrees(theta2_rad), 2),
            round(math.degrees(theta3_rad), 2)
        )

if __name__ == "__main__":
    arm = RoboticArm3DOF(L1=10.0, L2=8.0, L3=5.0)
    x, y, phi = arm.forward_kinematics(35, 45, -30)
    print(f"Forward Kinematics -> End-Effector: X={x} cm, Y={y} cm, Phi={phi} deg")
    target = (12.79, 17.45, 50.0)
    sol = arm.inverse_kinematics(*target)
    print(f"Inverse Kinematics -> Joint Angles: {sol}")
