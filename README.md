# Progree Internship Tasks - Engineering Submission Archive

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![Organization: Progree](https://img.shields.io/badge/Organization-Progree-blueviolet.svg)](https://github.com/Shaayan-shah)

Engineering implementation files and documentation deliverables for the Progree Internship Program across two technical specializations: Robotics & Automation and Artificial Intelligence.

---

## Technical Tracks Overview

### 1. Robotics and Automation Track
Focuses on embedded control loops, kinematic solvers, and industrial factory automation logic:
* Task 1: Internship Announcement and Project Scope Documentation
* Task 2: Closed-Loop PID Line Follower Simulation (Python dynamic simulator and Arduino C++ embedded firmware)
* Task 3: 3-DOF Robotic Arm Kinematics Engine (Analytical forward and geometric inverse kinematics)
* Task 4: Smart Industrial Conveyor and Sorting Grid (Arduino PLC sequence logic and edge telemetry logger)

### 2. Artificial Intelligence Track
Focuses on natural language processing, deterministic heuristic pathfinding, and computer vision segmentation:
* Task 1: Technical Announcement and Architecture Overview
* Task 2: Multi-Class Text Sentiment Classifier (TF-IDF vectorizer and regularized linear classifier)
* Task 3: Heuristic Graph Pathfinding Engine (A* and Dijkstra search from first principles)
* Task 4: Real-Time Computer Vision Object Detection Pipeline (Adaptive contour segmentation, shape approximation, and low-latency feature tracking)

---

## Repository Structure

```
Progree_Internship_Tasks/
|-- requirements.txt
|-- LICENSE
|-- .gitignore
|-- README.md
|-- test_all.py
|-- Robotics_and_Automation/
|   |-- Task_1_LinkedIn_Announcement/
|   |   |-- Task_1_LinkedIn_Announcement.docx
|   |   |-- Task_1_LinkedIn_Announcement.pdf
|   |   `-- linkedin_post_caption.txt
|   |-- Task_2_Closed_Loop_PID_Simulation/
|   |   |-- pid_simulation.py
|   |   |-- tinkercad_arduino_pid_line_follower.ino
|   |   |-- pid_response_curve.png
|   |   |-- Task_2_PID_Control_System_Report.docx
|   |   `-- Task_2_PID_Control_System_Report.pdf
|   |-- Task_3_Robotic_Arm_Kinematics/
|   |   |-- robotic_arm_3dof_kinematics.py
|   |   |-- kinematics_3dof_diagram.png
|   |   |-- Task_3_Robotic_Arm_Kinematics_Report.docx
|   |   `-- Task_3_Robotic_Arm_Kinematics_Report.pdf
|   `-- Task_4_Smart_Industrial_Automation_Grid/
|       |-- smart_conveyor_plc_logic.ino
|       |-- telemetry_edge_logger.py
|       |-- circuit_and_flow_diagram.png
|       |-- Task_4_Industrial_Automation_Grid_Report.docx
|       `-- Task_4_Industrial_Automation_Grid_Report.pdf
`-- Artificial_Intelligence/
    |-- Task_1_LinkedIn_Announcement/
    |   |-- Task_1_LinkedIn_Announcement.docx
    |   |-- Task_1_LinkedIn_Announcement.pdf
    |   `-- linkedin_ai_post_caption.txt
    |-- Task_2_Sentiment_Classifier_NLP/
    |   |-- sentiment_classifier.py
    |   |-- sample_sentiment_dataset.csv
    |   |-- confusion_matrix_plot.png
    |   |-- Task_2_Sentiment_Classifier_Report.docx
    |   `-- Task_2_Sentiment_Classifier_Report.pdf
    |-- Task_3_Pathfinding_Search_Engine/
    |   |-- pathfinding_search_engine.py
    |   |-- pathfinding_grid_result.png
    |   |-- Task_3_Pathfinding_Search_Engine_Report.docx
    |   `-- Task_3_Pathfinding_Search_Engine_Report.pdf
    `-- Task_4_Computer_Vision_Pipeline/
        |-- vision_detector_pipeline.py
        |-- sample_test_image.png
        |-- detection_output_preview.png
        |-- Task_4_Computer_Vision_Pipeline_Report.docx
        `-- Task_4_Computer_Vision_Pipeline_Report.pdf
```

---

## Installation and Setup

### Prerequisites
* Python 3.10 or higher
* Git

### Dependencies
Install the required packages using pip:

```bash
pip install -r requirements.txt
```

Core dependencies include:
* `numpy`: Vectorized math and array operations
* `pandas`: Tabular dataset ingestion and preprocessing
* `scikit-learn`: Feature extraction, train-test splitting, and evaluation metrics
* `opencv-python`: Image filtering, contour detection, and visual annotation

---

## Execution Guide

All scripts can be executed directly from the repository root directory.

### Automated Verification Suite
Run the full verification test suite covering all robotics, kinematics, search algorithms, and machine learning pipelines:
```bash
python test_all.py
```

### Robotics and Automation

1. Closed-Loop PID Line Follower Simulation:
```bash
python Robotics_and_Automation/Task_2_Closed_Loop_PID_Simulation/pid_simulation.py
```

2. 3-DOF Robotic Arm Forward and Inverse Kinematics:
```bash
python Robotics_and_Automation/Task_3_Robotic_Arm_Kinematics/robotic_arm_3dof_kinematics.py
```

3. Edge Telemetry Logger:
```bash
python Robotics_and_Automation/Task_4_Smart_Industrial_Automation_Grid/telemetry_edge_logger.py
```

### Artificial Intelligence

1. NLP Sentiment Classification Pipeline:
```bash
python Artificial_Intelligence/Task_2_Sentiment_Classifier_NLP/sentiment_classifier.py
```

2. A* and Dijkstra Pathfinding Search Engine:
```bash
python Artificial_Intelligence/Task_3_Pathfinding_Search_Engine/pathfinding_search_engine.py
```

3. Computer Vision Contour Segmentation Pipeline:
```bash
python Artificial_Intelligence/Task_4_Computer_Vision_Pipeline/vision_detector_pipeline.py
```

---

## Author & Acknowledgments

* Author: Shaayan Shah ([@Shaayan-shah](https://github.com/Shaayan-shah))
* Program: Progree Internship Program (Artificial Intelligence and Robotics & Automation tracks)

---

## License

This repository is distributed under the [MIT License](LICENSE).
