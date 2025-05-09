# Advanced Autonomous Driving System

## Overview
This project implements an advanced autonomous driving system that integrates multiple functionalities such as lane detection, object detection, traffic density analysis, and vehicle tracking. The system processes video input to provide real-time insights and generates a detailed PDF report summarizing the results.

## Features
- **Lane Detection**: Detects and highlights lanes on the road using computer vision techniques.
- **Object Detection**: Identifies and tracks objects such as cars, trucks, buses, and pedestrians using the YOLO model.
- **Traffic Density Analysis**: Calculates traffic density based on the number of detected vehicles and the region of interest (ROI) area.
- **Vehicle Tracking**: Tracks vehicles across frames and calculates their speeds.
- **Collision Warnings**: Issues warnings for potential collisions based on proximity and speed.
- **Dashboard Overlay**: Displays real-time statistics such as FPS, steering angle, traffic density, and object counts.
- **PDF Report Generation**: Summarizes detection, lane, speed, traffic, and self-driving performance statistics in a PDF report.

## Requirements
- Python 3.8 or later
- OpenCV
- NumPy
- SciPy
- ReportLab
- Ultralytics YOLO

## Installation
1. Clone the repository or download the project files.
2. Install the required Python packages:
   ```cmd
   pip install opencv-python-headless numpy scipy reportlab ultralytics
   ```

## Usage
1. Place the video file to be processed in the project directory.
2. Update the `video_path` variable in `inference.py` with the path to your video file.
3. Run the script:
   ```cmd
   python inference.py
   ```
4. The system will process the video, display real-time results, and save a PDF report in the project directory.

## Output
- **Real-Time Display**: The system shows the processed video with lane markings, object detections, and a dashboard overlay.
- **PDF Report**: A detailed summary report is generated in the project directory with statistics on detections, lane performance, traffic density, and more.

## Key Functions
- `process_lane_detection(frame)`: Detects lanes in the given video frame.
- `draw_lanes(frame, lines, height, width, roi_vertices)`: Draws detected lanes on the frame.
- `calculate_steering_angle(lines, width)`: Calculates the steering angle based on lane positions.
- `analyze_traffic_density(total_vehicles, roi_area)`: Analyzes traffic density.
- `VehicleTracker`: Tracks vehicles and calculates their speeds.
- `draw_dashboard(frame, ...)`: Draws a dashboard overlay with real-time statistics.
- `create_pdf_report(...)`: Generates a PDF report summarizing the results.

## Notes
- Ensure that the YOLO model file (`m_model.pt`) is available in the project directory.
- The system assumes a speed limit of 80 km/h for detecting speed violations.
- The PDF report includes detailed statistics on object detection, lane detection, speed analysis, traffic analysis, and self-driving performance.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- [Ultralytics YOLO](https://github.com/ultralytics/yolov5) for the object detection model.
- OpenCV and NumPy for computer vision and numerical computations.
- ReportLab for PDF generation.
