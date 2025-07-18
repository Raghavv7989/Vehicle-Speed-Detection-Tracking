# Vehicle Speed Detection & Tracking with YOLOv5

A real-time, single-camera vehicle speed detection and tracking system using YOLOv5, a custom centroid/Kalman-based tracker, and pixel-to-real-world calibration for accurate speed estimation. Designed for traffic monitoring, law enforcement, and research.

---

## Features

- **Vehicle Detection**: State-of-the-art YOLOv5 model for reliable car detection.
- **Tracking**: Custom, fast, and smooth tracker (centroid/Kalman) for maintaining vehicle IDs and paths.
- **Speed Estimation**: Accurate speed computation using camera calibration.
- **Violation Highlighting**: Visual alerts for vehicles exceeding set speed limits.
- **Real-Time Processing**: Optimized for live or recorded video streams.
- **Minimal Dependencies**: Pure Python implementation for easy deployment and extension.

## Usage

1. **Install Dependencies**  
pip install torch opencv-python yolov5
text

2. **Set Video Path**  
Edit `config.py` with your video file path.

3. **Calibrate for Accuracy**  
Adjust the `pixels_to_meters` ratio in `main.py` using a known distance in your video.

4. **Run the Project**  
python main.py
text

5. **View Results**  
The video window will display detected vehicles with IDs, speeds, and speed-limit violators highlighted in red.

## Project Structure

vehicle_speed_detection/
│
├── main.py # Main orchestration script
├── detector.py # YOLOv5 vehicle detection
├── tracker.py # Custom vehicle tracker
├── speed_estimator.py # Speed computation logic
├── helpers.py # Utility & I/O functions
├── config.py # Configuration (paths, thresholds)
├── outputs/ # Processed videos/logs storage
└── requirements.txt # Dependencies
text

## Customization

- **Detection Model**: Swap in any YOLOv5 variant or fine-tune on your dataset.
- **Tracking Logic**: Extend or replace the tracker for advanced scenarios (occlusion, multi-camera).
- **Calibration**: For best results, calibrate using a known real-world distance in your video.
- **Logging**: Add CSV or database logging for violations and analytics.

## Limitations

- **Single Camera**: Optimized for fixed, single-camera setups.
- **Calibration Dependency**: Speed accuracy relies on correct camera calibration.
- **Lighting/Weather**: Performance may vary in poor visibility conditions.

## Future Improvements

- **Multi-Camera Support**
- **Advanced Tracking**: SORT/DeepSORT integration
- **Edge Deployment**: Optimize for embedded systems or IoT devices

## References

- **YOLOv5**: https://github.com/ultralytics/yolov5
- **OpenCV**: https://opencv.org/
- **Kalman Filter Tracking**: Standard computer vision practice for smooth object tracking

## License

[Choose your license, e.g., MIT]

---

**Feel free to contribute, fork, or adapt this project for your needs!**
