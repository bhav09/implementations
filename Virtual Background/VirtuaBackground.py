import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
import numpy as np

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
segment_obj = SelfiSegmentation()
count = 0
list_imgs = os.listdir('Images')
while True:
    imgbg = cv2.imread(f'Images/{list_imgs[count%len(list_imgs)]}')
    _,img = cam.read()
    img = cv2.flip(img,1)
    output = segment_obj.removeBG(img,imgbg,threshold=0.3)
    final = np.hstack([img,output])
    cv2.imshow('Window',final)
    key = cv2.waitKey(1)
    if key == ord('a'):
        count += 1
    elif key == ord('d'):
        count -= 1
    elif key == ord('q'):
        break


