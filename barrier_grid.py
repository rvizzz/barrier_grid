import cv2 as cv
import numpy as np
import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("video_file", help="video file to make an animation of")
parser.add_argument("-w", type=int, help="width in pixels of the vertical slices from the video frame")
parser.add_argument("-f", type=int, help="number of frames from the input video (should be small (~4))")
parser.add_argument("-s", type=int, help="number of frames to skip after writing a frame from the video file")
parser.add_argument("-t", type=float, help="width in pixels that will be transparent in the transparency print out")
args = parser.parse_args()

file_name = args.video_file

pixel_window = 6
num_frames = 4
skip_frames = 0
template_gap = pixel_window * 1.5

if args.w:
    pixel_window = args.w

if args.f:
    num_frames = args.f

if args.s:
    skip_frames = args.s
    
if args.t:
    template_gap = args.t


cap = cv.VideoCapture(file_name)

width = int(cap.get(3))
height = int(cap.get(4))

output_image = np.zeros((height, width, 3), dtype = np.uint8)
output_image[:] = [255, 255, 255]

output_transparency = np.zeros((height, width, 3), dtype = np.uint8)

block_size = pixel_window * num_frames

print("Video file: " + file_name)
print("Pixel window: " + str(pixel_window))
print("Number of frames: " + str(num_frames))
print("Transparency gap width: " + str(template_gap))
print("Writing 1 in every " + str(skip_frames + 1) + " frames")

file_suffix = str(pixel_window) + "_" + str(num_frames) + "_" + str(skip_frames) + "_" + str(template_gap)


for i in range(num_frames):
    ret, frame = cap.read()
    
    if not ret:
        break;
        
    for skip in range(skip_frames):
        cap.read()
    
    
    for j in np.arange(0, width, block_size):
        
        window_start = int(j + pixel_window * i)
        window_end = int(j + pixel_window * (i + 1))
        
        output_image[0:height, window_start:window_end] = frame[0:height, window_start:window_end]
        
        
for i in np.arange(0, width, block_size):
    window_start = int(i)
    window_end = int(i + template_gap)
    
    output_transparency[0:height, window_start:window_end] = [255, 255, 255]
    
cv.imwrite("image." + file_suffix + ".png", output_image)
cv.imwrite("transparency." + file_suffix + ".png", output_transparency)

out_demo_stream = cv.VideoWriter("vid_demo." + file_suffix + ".mp4", cv.VideoWriter_fourcc('m','p','4','v'), 30.0, (width, height), 1)

for i in range(int(block_size)):
    
    output_test_frame = np.zeros((height, width, 3), dtype = np.uint8)
    output_test_frame[:] = [255, 255, 255]
    
    for j in np.arange(0, width, block_size):
    
        window_start = int(j + i)
        window_end = int(j + template_gap + i)
    
        output_test_frame[0:height, window_start:window_end] = output_image[0:height, window_start:window_end]
    
    out_demo_stream.write(output_test_frame)
    
out_demo_stream.release()
