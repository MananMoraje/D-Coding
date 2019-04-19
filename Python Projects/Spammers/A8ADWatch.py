import pyautogui as py
import time

time.sleep(10)
py.mouseDown(1290, 110)
py.mouseUp(1290, 110)
time.sleep(2)
while True:
    py.mouseDown(1200, 650)
    py.mouseUp(1200, 650)
    time.sleep(60)
    py.mouseDown(1290, 50)
    py.mouseDown(1290, 50)
    time.sleep(2)
    py.mouseDown(700, 300)
    py.mouseUp(700, 300)
    time.sleep(7)

