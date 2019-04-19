import pyautogui
import time

time.sleep(9)
while True:
    time.sleep(1)
    pyautogui.keyDown('right')
    pyautogui.keyUp('right')
    i = 0
    while i != 5:
        time.sleep(1)
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

