import cv2
import random
import os
import json

path = '/Users/swarajpanchal/Desktop/Sem 5/xyz/img/'
output_path = '/Users/swarajpanchal/Desktop/Sem 5/xyz/vid/'
output_video_name = 'sunset.mp4'
output_video_full_path = output_path + output_video_name

pre_imgs = os.listdir(path) #for making an array of images in memory
# print(pre_imgs)
img = [] #creating empty array of images

for i in pre_imgs:  #loop for pre_images
    i = path+i 
    # print(i) 
    img.append(i)

# print(img)

cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v') #in open cv2 thier is videowiter function for making video
frame = cv2.imread(img[0]) #frame of images (border of image)

size = list(frame.shape) #width and height of image array
# print(size)
# exit()
del size[2] #deleting 3rd element of size
#size.reverse() 
# print(size)

video = cv2.VideoWriter(output_video_full_path, cv2_fourcc, 1, size) #output: video name, fourcc, fps, size (videowriter is class of cv2 and creating object and passing the required arrguments)
counter = 0 
imgsizes = [2,0,3,4,1]# frame time in seconds of individual frames
#print(img)
data= dict(zip(img, imgsizes))#creating a dictionary of images and its frame type
#looping through data dictionary to get a corresponding img and its frame type
for sp ,img_size in data.items(): #inserting frames into the video object 
    print('frame', counter+1, 'of', len(img))
    counter+=1
    for i in range (img_size):
        print('fps', i)
        video.write(cv2.imread(sp))
    # with open(sp) as f:
    #     #checking for the img file extention (.jpeg)
    #     if f.name.endswith('.jpeg'):
    # #         for j in range(random.randint(1,9)):
    #         for i in range (0,img_size):
    #             print('fps', i)
    #             video.write(cv2.imread(sp))
# print(data)
# exit()

video.release() #relase video into the given path