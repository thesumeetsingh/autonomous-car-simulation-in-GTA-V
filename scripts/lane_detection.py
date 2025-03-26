import cv2
import numpy as np

class LaneDetector:
    def __init__(self):
        pass

    def region_of_interest(self, img):
        height, width = img.shape[:2]
        mask = np.zeros_like(img)
        polygon = np.array([
            [
                (50, height),
                (width // 2 - 50, height // 2),
                (width // 2 + 50, height // 2),
                (width - 50, height)
            ]
        ], np.int32)
        
        cv2.fillPoly(mask, polygon, 255)
        return cv2.bitwise_and(img, mask)

    def detect_lanes(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blur, 50, 150)
        roi = self.region_of_interest(edges)
        
        lines = cv2.HoughLinesP(roi, 1, np.pi / 180, 50, minLineLength=100, maxLineGap=50)
        
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

        return frame