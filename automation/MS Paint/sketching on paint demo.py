import pyautogui
import time
import cv2
import numpy as np

pyautogui.FAILSAFE = True
#time.sleep(3)

video = cv2.VideoCapture(0)
'''
#video.set(3,500)
#video.set(4,500)'''
video.set(10,100)
while True:
    _,img = video.read()
    img_flip = cv2.flip(img,1) #flipping the image
    cv2.imshow('Video',img_flip)
    if cv2.waitKey(1) == 27:
        image = img_flip
        break
video.release()
cv2.destroyAllWindows()

canny = cv2.Canny(image,130,180)
print(canny.shape)
print(np.unique(canny))
cv2.imshow('Canny',canny)
cv2.waitKey(3000)
time.sleep(4)
pyautogui.click()
for i in range(100,canny.shape[0]):
    for j in range(100,canny.shape[1]):
        if canny[i][j] == 255:
            pyautogui.moveTo(j+300,i+300,duration=0.000000001)
            pyautogui.click()

cv2.imshow('Edges',canny)
cv2.imshow('Captured Image',image)
cv2.waitKey(0)
