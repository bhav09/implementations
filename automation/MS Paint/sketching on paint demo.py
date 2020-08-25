# GuideLine : 
#if you want to terminate the automation in midst of it, press alt+ctrl+del, then escape key.
#it approximately takes 15-18 mins depending upon the edges it is detecting , so please be patient. 

import pyautogui
import time
import cv2
import numpy as np

pyautogui.FAILSAFE = True
#time.sleep(3)

video = cv2.VideoCapture(0)
'''
#video.set(3,500)
#video.set(4,500)
'''
video.set(10,100)
while True:
    _,img = video.read()
    img_flip = cv2.flip(img,1) #flipping the image
    cv2.imshow('Video',img_flip)
    if cv2.waitKey(1) == 27: #press escape to capture the picture from the live video 
        image = img_flip
        break
video.release()
cv2.destroyAllWindows()

canny = cv2.Canny(image,130,180) #these are thresholds , one can vary these thresholds. In my case it worked for a range of (50,180) bcz I had a plane background.
print(canny.shape)
print(np.unique(canny))
cv2.imshow('Canny',canny)
cv2.waitKey(3000)
time.sleep(4) #now you have a time of 4 seconds to go to your paint window, it is advised to keep it open in the background so that that a lot of time isn't wasted.
pyautogui.click()

#you can alter this loop to a dict so as to see other variations. 
for i in range(100,canny.shape[0]):   #you can change 100 to 0, I kept it 100 so as to remove the line that comes on the top.
    for j in range(100,canny.shape[1]):
        if canny[i][j] == 255:
            pyautogui.moveTo(j+300,i+300,duration=0.0000001) 
            pyautogui.click()

cv2.imshow('Edges',canny)
cv2.imshow('Captured Image',image)
cv2.waitKey(0)
