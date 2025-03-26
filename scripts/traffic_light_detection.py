import cv2
import torch
from ultralytics import YOLO

class TrafficLightDetector:
    def __init__(self):
        self.model = YOLO('models/yolov8_traffic.pt')
        self.class_names = {0: 'Red', 1: 'Yellow', 2: 'Green'}  # Class labels for the model

    def detect_traffic_light(self, frame):
        results = self.model.predict(frame)

        for result in results:
            for box in result.boxes.data:
                x1, y1, x2, y2, conf, cls = box.tolist()
                label = self.class_names.get(int(cls), "Unknown")
                color = (0, 0, 255) if label == 'Red' else (0, 255, 255) if label == 'Yellow' else (0, 255, 0)

                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
                cv2.putText(frame, f'{label} ({conf:.2f})', (int(x1), int(y1) - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                return label

        return None
