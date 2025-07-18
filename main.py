# main.py
import cv2
import time
from config import VIDEO_PATH, SPEED_THRESHOLD
from detector import VehicleDetector
from tracker import CentroidTracker
from speed_estimator import SpeedEstimator
from helpers import load_video, display_frame, draw_bboxes_ids


def main():
    cap = load_video(VIDEO_PATH)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # ---- Calibration (Modify these values based on your video) ----
    # Example: If 50 pixels in video = 3.7 meters in real life (lane width)
    real_width_meters = 3.7
    pixel_width = 50
    pixels_to_meters = real_width_meters / pixel_width
    # Adjust based on your video for accurate speed!

    detector = VehicleDetector()
    tracker = CentroidTracker(max_disappeared=5)
    speed_estimator = SpeedEstimator(fps, pixels_to_meters)

    window_name = "Vehicle Speed Detection"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect vehicles
        detections = detector.detect(frame)
        bboxes = [det[:4] for det in detections]
        objects = tracker.update(bboxes)

        # Estimate speed for each tracked vehicle
        speeds = speed_estimator.estimate(objects, frame)

        # Draw bounding boxes, IDs, and speeds
        frame_with_boxes = draw_bboxes_ids(frame.copy(), objects, speeds, SPEED_THRESHOLD)

        # Display
        if display_frame(window_name, frame_with_boxes):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
