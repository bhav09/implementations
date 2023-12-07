import cv2
import keyboard
import mediapipe as mp
import time
import numpy as np
import math

class HandGestureRecognition:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
        self.prev_time, self.curr_time = 0, 0

    def calculate_slope(self, x1, y1, x2, y2):
        return (y2 - y1) / (x2 - x1)

    def calculate_angle(self, s1, s2):
        return math.degrees(math.atan((s2 - s1) / (1 + (s2 * s1))))

    def run(self):
        while True:
            _, img = self.cam.read()
            img = cv2.flip(img, 1)
            img1 = img.copy()

            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = self.hands.process(imgRGB)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mpDraw.draw_landmarks(img, hand_landmarks, self.mpHands.HAND_CONNECTIONS)

                myHand = results.multi_hand_landmarks[0]
                lmlist = myHand.landmark

                for id, lm in enumerate(lmlist):
                    h, w, c = img.shape

                    index_finger_tip = np.array([int(lmlist[8].x * w), int(lmlist[8].y * h)])
                    middle_finger_tip = np.array([int(lmlist[12].x * w), int(lmlist[12].y * h)])

                    dist = np.linalg.norm(index_finger_tip - middle_finger_tip)
                    centre = (index_finger_tip + middle_finger_tip) // 2
                    wrist = [int(lmlist[0].x * w), int(lmlist[0].y * h)]
                    cv2.line(img1, wrist, [wrist[0], wrist[1] - 800], (255, 0, 0), 4)

                    lineA = [wrist, list(centre)]
                    lineB = [wrist, [wrist[0] - 1, wrist[1] - 800]]

                    if dist < 120:
                        cv2.circle(img, (index_finger_tip + middle_finger_tip) // 2, 20, (255, 0, 0), -1)
                        cv2.circle(img1, (index_finger_tip + middle_finger_tip) // 2, 20, (255, 0, 0), -1)
                        slope1 = self.calculate_slope(lineA[0][0], lineA[0][1], lineA[1][0], lineA[1][1])
                        slope2 = self.calculate_slope(lineB[0][0], lineB[0][1], lineB[1][0], lineB[1][1])
                        ang = self.calculate_angle(slope1, slope2)
                        print('Angle in degrees = ', ang)

                        if ang > 20:
                            print('Left')
                            keyboard.press_and_release('left')
                        elif ang < -10:
                            print('Right')
                            keyboard.press_and_release('right')

            self.curr_time = time.time()
            fps = 1 / (self.curr_time - self.prev_time)
            self.prev_time = self.curr_time

            cv2.putText(img, f'FPS:{str(int(fps))}', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 2)
            cv2.imshow('Frames', img1)

            if cv2.waitKey(1) == ord('q'):
                break

if __name__ == "__main__":
    gesture_recognition = HandGestureRecognition()
    gesture_recognition.run()
