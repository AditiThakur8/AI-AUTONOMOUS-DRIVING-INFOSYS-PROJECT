import cv2
import os

frame_path = 'C:/Users/DELL/Downloads/frame.png'  # full path to your image
video_filename = 'urban_driving_scene.mp4'
fps = 30

frame = cv2.imread(frame_path)
height, width, layers = frame.shape

video = cv2.VideoWriter(video_filename, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

# write the same frame multiple times just to create a test video
for _ in range(90):  # 3 seconds of video
    video.write(frame)

video.release()
