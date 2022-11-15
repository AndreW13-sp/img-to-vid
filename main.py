import cv2
import os
import numpy as np
fps = 20.0
# path = 'C:\\Users\\HP\\Desktop'
path = '/Users/swarajpanchal/Desktop/Sem 5/xyz'
vid_name = 'Test.mp4'
list_ext = ['jpeg', 'jpg', 'png']
dic_dur = {'fast':1, 'medium': 2, 'slow': 4}
images = []
for file in os.listdir(os.path.join(path,'img')): 
    if file.split('.')[1] in list_ext:
       # print(file)
        images.append(os.path.join(path,'img',file))
img_dur = ['medium', 'slow', 'fast', 'medium']

cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')
frame = cv2.imread(images[0])  # frame of images (border of image)
        # print(frame)
        # exit()
size = list(frame.shape)
video = cv2.VideoWriter(os.path.join(path, vid_name), cv2_fourcc, fps, (size[1], size[0]))

for img_url, dur in zip(images, img_dur):
    t = dic_dur[dur]
    img = cv2.imread(img_url)
    # print(int(t*fps))
    for i in range(int(t*fps)):
        video.write(img)
video.release()