# speed_estimator.py
import numpy as np
from collections import defaultdict

class SpeedEstimator:
    def __init__(self, fps, pixels_to_meters):
        self.history = defaultdict(list)
        self.fps = fps
        self.pixels_to_meters = pixels_to_meters
        self.frame_count = 0

    def estimate(self, objects, frame):
        self.frame_count += 1
        speeds = {}

        for obj_id, obj in objects.items():
            centroid = obj['centroid']
            self.history[obj_id].append((self.frame_count, centroid))

            if len(self.history[obj_id]) < 2:
                continue

            # Take the current and the previous centroids
            p1 = np.array(self.history[obj_id][-2][1])
            p2 = np.array(self.history[obj_id][-1][1])
            pixel_distance = np.linalg.norm(p2 - p1)

            # Only calculate speed if there is movement
            if pixel_distance > 0:
                frames_elapsed = self.history[obj_id][-1][0] - self.history[obj_id][-2][0]
                time_elapsed = frames_elapsed / self.fps
                meters_distance = pixel_distance * self.pixels_to_meters
                speed_mps = meters_distance / time_elapsed
                speed_kmph = speed_mps * 3.6  # m/s to km/h
                speeds[obj_id] = speed_kmph

        return speeds
