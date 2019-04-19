import pyautogui
import random

while True:
    i = random.randint(0, 2000)
    ii = random.randint(0, 2000)
    pyautogui.mouseDown(i, ii)