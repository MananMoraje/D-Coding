import pyautogui
import time

m = input('Message:     ')
while True:
    #  Message
    time.sleep(0.7)
    pyautogui.mouseDown(300, 700)
    pyautogui.mouseUp(300, 700)
    time.sleep(0.5)
    pyautogui.typewrite(m)
    #  Send
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

