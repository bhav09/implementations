import keyboard
import pyautogui
import time

time.sleep(2)

pyautogui.moveTo(x=1000,y=400)
pyautogui.click()
#print(pyautogui.position())
keyboard.write('Day 315 of #dailycoding\n'
               'This post is a demonstration of how can one use automation to write paragraphs for LinkedIn Post, blogs, tweets etc.\n'
               '\nWe are using the following modules to implement it\n'
               '1. Time\n'
               '2. Pyautogui\n'
               '3. Keyboard\n'
               '\nLink to code and resources in the comments\n'
               '\nFollow Bhavishya pandit',delay=1/30)

time.sleep(1)
keyboard.press('down')
keyboard.press_and_release('enter')

keyboard.write(' #100dayprogrammingchallenge for a daily dose of code and learning!\n'
               '#ml #python #ai #automation #learning #100daysofcode #datascience #100daysofcoding',delay=1/30)