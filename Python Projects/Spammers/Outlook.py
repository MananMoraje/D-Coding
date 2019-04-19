import pyautogui
import time

i = input('Email Address:   ')
m = input('Message:     ')
j = 0
while True:
    j += 1
    print(str(j))
    #  New Button
    pyautogui.mouseDown(10, 100)
    pyautogui.mouseUp(10, 100)
    time.sleep(1)
    #  E-mail Address
    pyautogui.mouseDown(600, 100)
    pyautogui.mouseUp(600, 100)
    pyautogui.typewrite(i)
    time.sleep(1)
    #  Message
    pyautogui.mouseDown(600, 300)
    pyautogui.mouseUp(600, 300)
    pyautogui.typewrite(m)
    time.sleep(1)
    #  Send
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
