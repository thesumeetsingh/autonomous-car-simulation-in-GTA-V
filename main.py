import cv2
from scripts.lane_detection import LaneDetector
from scripts.vehicle_detection import VehicleDetector
# from scripts.traffic_light_detection import TrafficLightDetector
from scripts.control_car import move_car

def main():
    cap = cv2.VideoCapture(0)  # For webcam input
    lane_detector = LaneDetector()
    #traffic_light_detector = TrafficLightDetector()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error: Couldn't access camera.")
            break

        # Lane detection
        lane_frame = lane_detector.detect_lanes(frame)

        # Vehicle detection
        vehicle_frame = VehicleDetector(frame)

        # Traffic light detection
        #traffic_signal = traffic_light_detector.detect_traffic_light(frame)

        # Determine driving action
        lane_offset = 0  # Default no lane deviation
        vehicle_in_front = False
        
        # if traffic_signal == "Red":
        #     vehicle_in_front = True  # Stop the car
        # elif traffic_signal == "Yellow":
        #     pass  # Ready, proceed with caution
        # elif traffic_signal == "Green":
        #     pass  # Continue driving

        move_car(lane_offset, vehicle_in_front)

        # Display the result
        cv2.imshow('Lane & Vehicle Detection', vehicle_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
