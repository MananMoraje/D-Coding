import pyautogui
import time
import pyscreenshot as pyss

while True:

    pyautogui.keyDown('right', 0.1)
    pyautogui.keyUp('right')
    time.sleep(00.05)
    print(pyss.about)

