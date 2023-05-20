import pyautogui
import keyboard
import random
import time

#Finding the chrome button on the taskbar
chromelocation = pyautogui.locateOnScreen('chrome.png', confidence = 0.8)
chromelocation = pyautogui.center(chromelocation)
print(chromelocation)

#Pressing the chrome button
pyautogui.click(chromelocation)

#waiting for 1 sec
time.sleep(2)

#Creating a new tab if chrome was already opened else click on the empty tab
if pyautogui.locateOnScreen('newtab.png', confidence = 0.7) == None:
    keyboard.send('ctrl+t')
else:
    newtablocation = pyautogui.locateCenterOnScreen('newtab.png', confidence = 0.7)
    pyautogui.click(newtablocation)