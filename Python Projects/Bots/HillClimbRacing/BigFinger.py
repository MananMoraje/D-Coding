import pyautogui
import time
from PIL import ImageGrab

time.sleep(7)


def mtnd():
    pyautogui.keyDown('right')


def drive():
    pyautogui.keyDown('right', 1)
    pyautogui.keyUp('right')
    time.sleep(1)


box = (960, 100, 1160, 250)
image = ImageGrab.grab(box)
i = 0

pixels = list(image.getdata())
width, height = image.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
i = 0

while True:
    while i < len(pixels):
        if pixels[i] != '#7EEAFF':
            mtnd()
        else:
            drive()
    i = 0
