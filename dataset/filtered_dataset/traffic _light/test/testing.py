import cv2
import os

frame_folder = r"C:\Users\DELL\Downloads\frame.png"
video_filename = 'urban_driving_scene.mp4'
fps = 30

images = [img for img in sorted(os.listdir(frame_folder)) if img.endswith(".png")]
frame = cv2.imread(os.path.join(frame_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_filename, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

for image in images:
    video.write(cv2.imread(os.path.join(frame_folder, image)))

video.release()
