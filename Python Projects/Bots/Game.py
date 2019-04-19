

from PIL import ImageGrab, ImageOps
import pyautogui
import time


class Co():
    replayBtn = (340, 300)
    dino = (171, 395)

 
def restart():
    pyautogui.click(Co.replayBtn)


def img():
    box = (Co.dino[0] + 80, Co.dino[1] + 20, Co.dino[0] + 140, Co.dino[1] + 40)
    image = ImageGrab.grab(box)
    grayimage = ImageOps.grayscale(image)
    a = (grayimage.getcolors())
    print(str(a))
    if str(a) == '[{1200, 247)]':
        c = 0
    else:
        pyautogui.keyDown(' ')



def main():
    restart()
    while True:
        img( )


main()








