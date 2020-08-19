import pyautogui
import time
#pyautogui.getActiveWindow().maximize() #maximize the active window
#pyautogui.getWindowsWithTitle()
time.sleep(3)
pyautogui.click()
x = 250
while x > 0:
    pyautogui.dragRel(x,0,duration=0.3)
    pyautogui.click()
    x -= 25
    pyautogui.dragRel(0,x,duration=0.3)
    pyautogui.click()
    x -= 25
    pyautogui.dragRel(-x,0,duration=0.2)
    pyautogui.click()
    x -= 25
    pyautogui.dragRel(0,-x,duration=0.2)
    x -= 25