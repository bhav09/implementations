import pyautogui
pyautogui.sleep(5)
#print(pyautogui.position())
pyautogui.moveTo(571,713,duration=0.4)
pyautogui.moveTo(727,647,duration=0.4)
pyautogui.click()
#scrolling feed
for i in range(20):
    pyautogui.scroll(-500)
    pyautogui.sleep(1)
pyautogui.sleep(3)
#print(pyautogui.position())
pyautogui.moveTo(592,546,duration=0.3)
pyautogui.moveTo(716,481,duration=0.3)
pyautogui.click()
pyautogui.moveTo(1915,0)
pyautogui.click()
