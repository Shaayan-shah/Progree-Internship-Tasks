# Progree Artificial Intelligence — Task 4
# Real-Time Computer Vision Object Detector & Frame-By-Frame Segmenter Pipeline

import os
import cv2
import time
import numpy as np

def run_vision_pipeline(image_path=None):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if image_path is None:
        image_path = os.path.join(script_dir, "sample_test_image.png")
    elif not os.path.isabs(image_path) and not os.path.exists(image_path):
        candidate = os.path.join(script_dir, image_path)
        if os.path.exists(candidate):
            image_path = candidate

    frame = cv2.imread(image_path)
    if frame is None:
        frame = np.ones((400, 600, 3), dtype=np.uint8) * 240
        cv2.circle(frame, (150, 200), 50, (220, 50, 50), -1)
        cv2.rectangle(frame, (320, 140), (440, 260), (50, 180, 50), -1)

    start_t = time.perf_counter()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 1.5)

    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    detected_targets = []
    output_frame = frame.copy()

    for idx, cnt in enumerate(contours):
        area = cv2.contourArea(cnt)
        if area > 300:
            x, y, w, h = cv2.boundingRect(cnt)
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)

            shape_label = "Polygon"
            if len(approx) == 3:
                shape_label = "Triangle"
            elif len(approx) == 4:
                shape_label = "Rectangle"
            elif len(approx) > 4:
                shape_label = "Circle"

            detected_targets.append({
                "id": idx + 1,
                "shape": shape_label,
                "area_px": area,
                "bbox": (x, y, w, h)
            })

            cv2.rectangle(output_frame, (x, y), (x + w, y + h), (0, 200, 255), 2)
            cv2.putText(
                output_frame, f"#{idx+1} {shape_label} ({int(area)}px)", (x, y - 8),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (15, 23, 42), 1, cv2.LINE_AA
            )

    latency_ms = (time.perf_counter() - start_t) * 1000
    fps = 1000.0 / latency_ms if latency_ms > 0 else 0.0

    cv2.putText(
        output_frame, f"Tracking: {len(detected_targets)} Targets | Latency: {latency_ms:.2f}ms ({fps:.1f} FPS)",
        (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (2, 132, 199), 2, cv2.LINE_AA
    )

    output_path = os.path.join(script_dir, "detection_output_preview.png")
    cv2.imwrite(output_path, output_frame)
    print(f"Pipeline executed in {latency_ms:.2f} ms ({fps:.1f} FPS). Extracted {len(detected_targets)} objects.")

if __name__ == "__main__":
    run_vision_pipeline()
