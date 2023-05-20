import pyautogui
import keyboard
import random
import time
import webbrowser

name = 

webbrowser.open('https://gogoanime.be/', new = 0)
print('Opened browser')

#Waiting for the site to load
time.sleep(5)
print('Waited 5 seconds')

def locate_searchbar():
    try:
        global searchloaction
        searchloaction = pyautogui.locateOnScreen('searchbar.png', confidence = 0.8)
        print('Searched for search bar')
        searchloaction = pyautogui.center(searchloaction)
        pyautogui.click(searchloaction)
        print('Clicked the search bar')
        #Closing ad tab if it appears
        if pyautogui.locateOnScreen('searchbar.png', confidence = 0.8) == None:
            keyboard.send('ctrl+w')
    except Exception:
        locate_searchbar()

#Searching for the search bar and clicking it
locate_searchbar()

#Searching for the anime
pyautogui.write(name, interval = 0.01)

time.sleep(2)
pyautogui.click(searchloaction.x,searchloaction.y + 100)
time.sleep(2)

#Getting site link
pyautogui.click(448, 48)
link = keyboard.send('ctrl+c')
print('Link Copied to Clipboard')

print('Typed the anime name')
