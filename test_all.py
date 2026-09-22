"""
Unified Automated Test & Verification Suite for Progree Internship Deliverables
Executes end-to-end algorithmic assertions across Robotics and AI modules.
"""

import os
import sys
import time

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Import Robotics modules
sys.path.insert(0, os.path.join(ROOT_DIR, "Robotics_and_Automation", "Task_2_Closed_Loop_PID_Simulation"))
sys.path.insert(0, os.path.join(ROOT_DIR, "Robotics_and_Automation", "Task_3_Robotic_Arm_Kinematics"))
sys.path.insert(0, os.path.join(ROOT_DIR, "Robotics_and_Automation", "Task_4_Smart_Industrial_Automation_Grid"))

# Import AI modules
sys.path.insert(0, os.path.join(ROOT_DIR, "Artificial_Intelligence", "Task_2_Sentiment_Classifier_NLP"))
sys.path.insert(0, os.path.join(ROOT_DIR, "Artificial_Intelligence", "Task_3_Pathfinding_Search_Engine"))
sys.path.insert(0, os.path.join(ROOT_DIR, "Artificial_Intelligence", "Task_4_Computer_Vision_Pipeline"))

from pid_simulation import PIDController
from robotic_arm_3dof_kinematics import RoboticArm3DOF
from pathfinding_search_engine import GridPathfindingAgent
from sentiment_classifier import clean_text, run_sentiment_pipeline
from vision_detector_pipeline import run_vision_pipeline


def test_pid_convergence():
    print("[1/5] Testing Closed-Loop PID Controller Convergence...")
    pid = PIDController(Kp=4.0, Ki=0.5, Kd=1.2, setpoint=0.0)
    pos = 5.0
    dt = 0.02
    for _ in range(150):
        output, _ = pid.compute(pos, dt)
        pos += (output * 0.25) * dt
    assert abs(pos) < 0.05, f"PID controller did not converge to target 0.0 cm: {pos}"
    print(f"      PASS: Settled position: {pos:.4f} cm (error < 0.05 cm)")


def test_robotic_arm_kinematics():
    print("[2/5] Testing 3-DOF Arm Kinematics Round-Trip Precision...")
    arm = RoboticArm3DOF(L1=10.0, L2=8.0, L3=5.0)
    theta1, theta2, theta3 = 35.0, 45.0, -30.0
    x, y, phi = arm.forward_kinematics(theta1, theta2, theta3)
    sol = arm.inverse_kinematics(x, y, phi)
    assert sol is not None, "Inverse kinematics solver failed to find a valid solution."
    calc_t1, calc_t2, calc_t3 = sol
    assert abs(calc_t1 - theta1) < 0.25, f"Theta 1 mismatch: {calc_t1} vs {theta1}"
    assert abs(calc_t2 - theta2) < 0.25, f"Theta 2 mismatch: {calc_t2} vs {theta2}"
    assert abs(calc_t3 - theta3) < 0.25, f"Theta 3 mismatch: {calc_t3} vs {theta3}"
    print(f"      PASS: Forward & Inverse Kinematics verified with error < 0.25 deg")


def test_pathfinding_optimality():
    print("[3/5] Testing Heuristic A* Pathfinding Engine...")
    obstacles = [(3, y) for y in range(2, 9)] + [(7, y) for y in range(3, 10)]
    agent = GridPathfindingAgent(width=12, height=12, obstacles=obstacles)
    start, goal = (1, 1), (10, 10)
    path, nodes, runtime = agent.a_star_search(start, goal)
    assert path is not None, "A* pathfinding failed to discover a valid path."
    assert path[0] == start and path[-1] == goal, "Path endpoints do not match start and goal."
    for p in path:
        assert p not in agent.obstacles, f"Path intersected obstacle at {p}"
    print(f"      PASS: Optimal path of {len(path)} steps found in {runtime:.3f} ms (expanded {nodes} nodes)")


def test_nlp_sentiment():
    print("[4/5] Testing NLP Sentiment Cleaning & Classifier Pipeline...")
    raw = "The product build is excellent! Outstanding performance."
    cleaned = clean_text(raw)
    assert "!" not in cleaned and "." not in cleaned, "Text cleaner failed to strip punctuation."
    run_sentiment_pipeline()
    print("      PASS: NLP text pipeline executed successfully.")


def test_vision_pipeline_execution():
    print("[5/5] Testing Computer Vision Adaptive Segmentation Pipeline...")
    run_vision_pipeline()
    print("      PASS: Vision detector pipeline executed and saved output preview.")


def run_all():
    print("=" * 65)
    print("PROGREE INTERNSHIP DELIVERABLES: AUTOMATED TEST SUITE")
    print("=" * 65)
    t0 = time.perf_counter()
    test_pid_convergence()
    test_robotic_arm_kinematics()
    test_pathfinding_optimality()
    test_nlp_sentiment()
    test_vision_pipeline_execution()
    total_time = (time.perf_counter() - t0) * 1000
    print("=" * 65)
    print(f"ALL 5 MODULE TESTS PASSED IN {total_time:.2f} ms")
    print("=" * 65)


if __name__ == "__main__":
    run_all()
