#dependencies

#pip install opencv-python
import cv2
#pip install mediapipe
import mediapipe as mp
import time

#ancillaries
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

def image():
    #reading the iamge
    img = cv2.imread('Images/obama.jpg')
    #resizing the image
    img = cv2.resize(img,(800,600))
    #converting BGR to RGB
    rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #processing to detect potential body land marks
    output = pose.process(rgb)
    #if landmarks are present, then show them
    if output.pose_landmarks:
            mpDraw.draw_landmarks(img, output.pose_landmarks,mpPose.POSE_CONNECTIONS)
    #displaying the final output
    cv2.imshow('Video Frame', img)
    #infinite delay
    cv2.waitKey(0)

def video():
    prev_time = 0
    cam = cv2.VideoCapture('Videos/Elon Musk dancing.mp4')
    try:
        while True:
            #reading image as frames
            _,img = cam.read()
            #converting BGR to RGB
            rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            #processing to detect potential body land marks
            output = pose.process(rgb)
            #if landmarks are present, then show them
            if output.pose_landmarks:
                mpDraw.draw_landmarks(img, output.pose_landmarks,mpPose.POSE_CONNECTIONS)
            #generating FPS count
            curr_time = time.time()
            fps = 1/(curr_time-prev_time)
            prev_time = curr_time
            #pasting text
            cv2.putText(img,f'FPS: {str(int(fps))}',(450,60),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
            #displaying the final output
            cv2.imshow('Video Frame', img)
            #delay of 1 mili second
            cv2.waitKey(1)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    #for video
    video()
    
    #for image
    #image()
