import cv2
import os
from pathlib import Path

IMG_PATH = Path('./img')
OUT_PATH = Path('./vid')


def main():
    vid_name = 'test.mp4'
    list_ext = ('jpeg', 'jpg')
    dict_dur = {'fast': 1, 'medium': 3, 'slow': 5}
    size = (214, 142)

    images = []
    for file in os.listdir(IMG_PATH):
        if file.split('.')[1] in list_ext:
            # resize image
            photo = cv2.imread(str(IMG_PATH / file))
            # resized = cv2.resize(photo, size)
            images.append(str(IMG_PATH/file))

    # img_dur = ['medium', 'slow', 'fast', 'medium']
    img_dur = [1, 3, 2, 5]

    cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    video = cv2.VideoWriter(str(OUT_PATH / vid_name), cv2_fourcc, 1, size)
    # for img in images:
    #     video.write(cv2.imread(img))
    data = dict(zip(images, img_dur))#creating a dictionary of images and its frame type
    # print(data)
    # exit()
    counter = 1
    for sp ,img_size in data.items(): #inserting frames into the video object 
        print('frame', counter+1, 'of', len(images))
        counter+=1
        for i in range (0, img_size):
            print('fps', i)
            video.write(cv2.imread(sp))
    video.release()

if __name__ == '__main__':
    main()
