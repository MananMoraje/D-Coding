import pyautogui
import time

i = input('Email Address:   ')
m = input('Message:     ')
while True:
    #  New Button
    pyautogui.mouseDown(20, 150)
    pyautogui.mouseUp(20, 150)
    time.sleep(1)
    #  E-mail Address
    pyautogui.mouseDown(100, 250)
    pyautogui.mouseUp(100, 250)
    pyautogui.typewrite(i)
    time.sleep(1)
    #  Message
    pyautogui.mouseDown(150, 450)
    pyautogui.mouseUp(150, 450)
    pyautogui.typewrite(m)
    #  Send
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyUp('ctrl')

