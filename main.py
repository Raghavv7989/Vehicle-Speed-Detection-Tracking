import sys
from pathlib import Path

# Dynamically add project root
FILE = Path(__file__).resolve()
ROOT = FILE.parent
sys.path.append(str(ROOT))

from yolo.detect import run_yolo_detection
from tracker.centroid_tracker import CentroidTracker
from app_utils.speed_estimator import SpeedEstimator
from app_utils.config import PPM, FPS


# === Run detection (You can change source to webcam, 0) ===
run_yolo_detection(source='test_video.mp4')  # <- Make sure this file exists

# === Load the detected output video ===
output_video_path = ROOT / "runs" / "exp" / "test_video.mp4"
if not output_video_path.exists():
    print(f"[ERROR] Output video not found: {output_video_path}")
    sys.exit(1)

cap = cv2.VideoCapture(str(output_video_path))

tracker = CentroidTracker()
speed_estimator = SpeedEstimator(PPM, FPS)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Dummy bounding boxes for test (replace with parsed YOLO detections)
    rects = [(100, 200, 200, 300), (400, 250, 500, 350)]

    objects = tracker.update(rects)

    for object_id, centroid in objects.items():
        speed = speed_estimator.estimate_speed(object_id, centroid)
        cv2.putText(frame, f"ID {object_id} Speed: {speed:.2f} km/h", (centroid[0], centroid[1]-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.circle(frame, tuple(centroid), 4, (0, 255, 0), -1)

    cv2.imshow("Vehicle Speed Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
