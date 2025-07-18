# utils.py
import cv2

def load_video(path):
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        raise ValueError("Could not open video")
    return cap

def display_frame(window_name, frame):
    cv2.imshow(window_name, frame)
    return cv2.waitKey(1) & 0xFF == ord('q')

def draw_bboxes_ids(img, objects, speeds, speed_threshold):
    for obj_id, obj in objects.items():
        x1, y1, x2, y2 = map(int, obj['bbox'])
        bbox_color = (0, 255, 0)  # Green
        text_color = (0, 0, 255)  # Red
        if obj_id in speeds and speeds[obj_id] > speed_threshold:
            bbox_color = (0, 0, 255)  # Red for violators
        # Draw bbox
        cv2.rectangle(img, (x1, y1), (x2, y2), bbox_color, 2)
        # Draw object ID and speed (if available)
        label = f"ID: {obj_id}"
        if obj_id in speeds:
            label += f", {speeds[obj_id]:.1f} km/h"
        cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, text_color, 2)
    return img
