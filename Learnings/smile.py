import cv2
import keyboard
import time

time.sleep(2)
def detect(gray, frame):
    global jump
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        #cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
            jump = True
    return frame

path = 'D:/Pre Trained Models/HaarCascades/haarcascade_smile.xml'
face_cascade = cv2.CascadeClassifier('D:/Pre Trained Models/HaarCascades/haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(path)
cam = cv2.VideoCapture(0)
jump = False
while True:
    jump = False
    _,frame = cam.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    # Displays the result on camera feed
    cv2.imshow('Video', canvas)
    if jump == True:
        keyboard.press('up')
        time.sleep(0.05)
        keyboard.release('up')
    # The control breaks once q key is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# Release the capture once all the processing is done.
cam.release()
cv2.destroyAllWindows()
