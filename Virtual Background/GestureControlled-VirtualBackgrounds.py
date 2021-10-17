import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
import numpy as np
import time
import HandTrackingModule as htm
import math

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

segment_obj = SelfiSegmentation()
count = 0
list_imgs = os.listdir('Images')
ptime = 0
detector = htm.handDetector(detectionCon=0.7)

while True:
    #reading frames from webcam
    _,img = cam.read()

    #detecting Hand Keypoints
    img = detector.findHands(img=img)
    lmList = detector.findPosition(img,draw=False)

    #finding coordinates of the hand key point
    if len(lmList) != 0:
        #coordinates of Keypoints: Index and Middle finger
        x1,y1 = lmList[7][1],lmList[7][2]
        x2, y2 = lmList[11][1], lmList[11][2]

        #Centre point
        cx,cy = (x1+x2)//2,(y1+y2)//2

        #length is the length of line
        length = math.hypot(x2-x1,y2-y1)
        #print(length)
        if length < 30:
            cv2.circle(img,(cx,cy),10,(0,255,0),cv2.FILLED)
            count += 1

    ctime = time.time()
    imgbg = cv2.imread(f'Images/{list_imgs[count % len(list_imgs)]}')
    img = cv2.flip(img,1)

    output = segment_obj.removeBG(img,imgbg,threshold=0.3)
    final = np.hstack([img,output])
    fps = 1/(ctime-ptime)
    ptime = ctime

    cv2.putText(final,f'FPS:{int(fps)+10}',(40,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),3)
    cv2.imshow('Window',final)
    key = cv2.waitKey(10)

    if key == ord('q'):
        break