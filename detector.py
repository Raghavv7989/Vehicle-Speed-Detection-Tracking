# detector.py
import numpy as np
# detector.py
import torch

class VehicleDetector:
    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        self.class_id = 2  # COCO class_id for 'car' (2 by default)
        # Remove .to('cuda') if you get CUDA errors (as discussed earlier)

    def detect(self, frame):
        results = self.model(frame)
        detections = results.xyxy[0].cpu().numpy()
        cars = [det for det in detections if det[5] == self.class_id]
        return cars
