# Progree Robotics & Automation — Task 4
# Edge IoT Telemetry Receiver & CSV Logger

import os
import json
import csv
import datetime

def simulate_telemetry_stream():
    sample_packets = [
        {"timestamp": datetime.datetime.now().isoformat(), "part": "PLASTIC_PART", "distance_cm": 8.4, "action": "STANDARD_LINE", "conveyor_rpm": 120},
        {"timestamp": datetime.datetime.now().isoformat(), "part": "METAL_PART", "distance_cm": 6.2, "action": "DIVERTER_A", "conveyor_rpm": 120},
        {"timestamp": datetime.datetime.now().isoformat(), "part": "JAM_ERROR", "distance_cm": 1.2, "action": "EMERGENCY_STOP", "conveyor_rpm": 0}
    ]

    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(script_dir, "telemetry_production_log.csv")
    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "part", "distance_cm", "action", "conveyor_rpm"])
        writer.writeheader()
        for p in sample_packets:
            writer.writerow(p)

    print(f"Logged {len(sample_packets)} telemetry packets into {csv_file}")

if __name__ == "__main__":
    simulate_telemetry_stream()
