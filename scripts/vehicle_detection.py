import cv2
import torch
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("models/yolov8n.pt")

def VehicleDetector(frame):
    height, width = frame.shape[:2]

    # Run YOLO object detection
    results = model(frame)[0]

    for result in results.boxes.data:
        x1, y1, x2, y2, conf, cls = result.numpy()
        
        # Ignore vehicles in the bottom center (player's car)
        if y1 > height * 0.7 and width * 0.3 < x1 < width * 0.7:
            continue

        # Draw bounding box
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)

    return frame
