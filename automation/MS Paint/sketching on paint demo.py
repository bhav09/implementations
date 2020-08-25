# GuideLine : Please do read the comments before running the code !
#if you want to terminate the automation in midst of it, press alt+ctrl+del, then escape key.
#it approximately takes 15-18 mins depending upon the edges it is detecting , so please be patient. 

#dependencies

import pyautogui #pip install pyautogui
import time #inbuilt
import cv2 #pip install opencv-python
import numpy as np #pip install numpy

pyautogui.FAILSAFE = True
#time.sleep(3) 3 sec delay

video = cv2.VideoCapture(0)
'''
#video.set(3,500) #width
#video.set(4,500) #height 
'''
video.set(10,100) #brightness 
while True:
    _,img = video.read()
    img_flip = cv2.flip(img,1) #flipping the image , mirror image (exceptional)
    cv2.imshow('Video',img_flip)
    if cv2.waitKey(1) == 27: #press escape to capture the picture from the live video 
        image = img_flip
        break
video.release() #releasing the video capture 
cv2.destroyAllWindows() #cleaning all the windows

canny = cv2.Canny(image,130,180) #these are thresholds , one can vary these thresholds. In my case it worked for a range of (50,180) bcz I had a plane background.
print(canny.shape) #printing the shape of the edged image.
print(np.unique(canny))
cv2.imshow('Canny',canny)
cv2.waitKey(3000) #Images will be theere on your screen for a time of 3 seconds
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
cv2.waitKey(0) #infinite delay , can terminate this by pressing escape key
