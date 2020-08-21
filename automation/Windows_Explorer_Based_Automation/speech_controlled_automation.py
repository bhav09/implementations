#dependencies
import speech_recognition as sr
import pyautogui
import os
import time

#to recog. the folder where we want intend to go.
def speech_control():
    global recog
    r = sr.Recognizer()
    mic = sr.Microphone()
    print('Now listening ..')
    #time.sleep(1)
    with mic as source:
        audio = r.listen(source)
        try:
            print('You said:', r.recognize_google(audio))
        except sr.UnknownValueError:
            print('Value unknown')
        except sr.RequestError:
            print('Request Error')
    recog = recog + str(r.recognize_google(audio))

#to close the window
def close_window():
    pyautogui.moveTo(610, 0, duration=0.7)
    pyautogui.moveTo(1910, 20, duration=0.7)
    pyautogui.click()

#to maximize the window
def maximize_window():
    pyautogui.moveTo(1510,25,duration=0.7)
    pyautogui.click()
    pyautogui.click()

#to minimize the window
def minimzie_window():
    pyautogui.moveTo(1510, 25, duration=0.7)
    pyautogui.click()
    pyautogui.click()

# recog the directions for the movement of the mouse
def Move_to_direction():
    global direction
    print('Direction Demo..')
    r2 = sr.Recognizer()
    mic2 = sr.Microphone()
    print('Now listening ..')
    # time.sleep(1)
    with mic2 as source:
        audio = r2.listen(source)
        try:
            print('You said:', r2.recognize_google(audio))
        except sr.UnknownValueError:
            print('Value unknown')
        except sr.RequestError:
            print('Request Error')
    direction = direction + str(r2.recognize_google(audio))

direction = ''
pixels = 300 #drift of 300 pixels
time.sleep(2) #delay of 2 seconds
#pyautogui.moveRel(300,0,duration=0.4)
for i in range(4):
    Move_to_direction()
    if direction == 'right':
        pyautogui.moveRel(pixels,0,duration=0.4)
    elif direction == 'left':
        pyautogui.moveRel(-pixels,0,duration=0.4)
    elif direction == 'up':
        pyautogui.moveRel(0,-pixels,duration=0.4)
    elif direction == 'down':
        pyautogui.moveRel(0,pixels,duration=0.4)
    direction = ''
    print()
pyautogui.click() #clicks on the screen
print('---------------------------------------')
recog = ''
#path = 'C:/Users'
print('Where do you want to transcend ?')
print('1.Desktop\n2.Downloads\n3.Documents') #menu 1
time.sleep(1)
speech_control()
folder = recog
#print(folder)
close = False
path = f'C:/Users/91884/{folder}'
path = os.path.realpath(path)
os.startfile(path)
pyautogui.sleep(3)

for i in range(3):
    print('---------------------------------------')
    print('Window Based Operations')
    print('1.Maximize the window\n2.Minimize the window\n3.Close the window')  # menu 2
    r1 = sr.Recognizer()
    mic1 = sr.Microphone()
    print('Now listening ..')
    time.sleep(1)
    with mic1 as source:
        audio = r1.listen(source)
        command = r1.recognize_google(audio)
        if command == 'close the window':
            print('Close ',command)
            close_window()
        if command == 'maximize the window':
            print('Maximize ',command)
            maximize_window()
        if command == 'minimize the window':
            print('Minimize ',command)
            minimzie_window()
    
