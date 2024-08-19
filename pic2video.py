import os
import cv2
import numpy as np

path = './gastroscopy/'
filelist = os.listdir(path)
filelist.sort(key=lambda x: int(x[:-4]))

fps = 24
size = (1120, 780)


video = cv2.VideoWriter("./20230314172435.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)


for item in filelist:
    if item.endswith('.jpg'):
        item = path + item
        print(item)
        img = cv2.imread(item)
        video.write(img)

video.release()
cv2.destroyAllWindows()