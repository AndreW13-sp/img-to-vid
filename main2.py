import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
path= Path('./img')
out_path='/vid'

# print(path)
# exit()
def main():

    vid_name='Test.mp4'

    list_ext=['jpeg','jpg']
    dict_dur={'fast':1, 'medium':3, 'slow':5}
    images=[]
    for file in os.listdir(path):
        # print(file)
        # exit()
        if file.split('.')[1] in list_ext:
          print(file)
        #resize image 
        resized = cv2.resize(cv2.imread(file), (214,142) , interpolation = cv2.INTER_AREA)
        images.append(os.path.join(path, resized))
        img_dur = ['medium', 'slow', 'fast', 'medium']
        cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        frame = cv2.imread(images[0])  # frame of images (border of image)
        # print(frame)
        # exit()
        size = list(frame.shape)
        del size[2]
        size.reverse()
        #print reverse
        video = cv2.VideoWriter(os.path.join(path, vid_name), cv2_fourcc, 1 , (214,142))
        # for img, dur in (images, img_dur):
        t = dict_dur['slow']
        #for i in range(t*1):
        for img in images:
            video.write(cv2.imread(img))
        video.release()
    vid_name='Test.mp4'

if __name__ == '__main__':
    main()