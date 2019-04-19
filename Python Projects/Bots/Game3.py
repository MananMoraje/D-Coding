import pyautogui
import time

a = input('X, Y, Z, x2 1digit no commas, no spaces... ')
p = input('where should I teleport to? Only 1 digit nums')
t = input('What block?')



pyautogui.mouseDown(300,600)
pyautogui.mouseUp(300, 600)

pyautogui.mouseDown(300, 300)
pyautogui.mouseUp(300, 300)

pyautogui.keyDown('/' + 't' + 'p' + 'space' + str(p[0]) + str(p[1]) + str(p[2]))
pyautogui.keyDown('/')
time.sleep(1)
pyautogui.keyDown('f')
pyautogui.keyDown('i')
pyautogui.keyDown('l')
pyautogui.keyDown('l')
time.sleep(1)
pyautogui.keyDown('space')
pyautogui.keyDown(str(a[0]))
pyautogui.keyDown('space')
pyautogui.keyDown(str(a[1]))
pyautogui.keyDown('space')
pyautogui.keyDown(str(a[2]))
pyautogui.keyDown('space')
pyautogui.keyDown(str(a[3]))
pyautogui.keyDown('space')
pyautogui.keyDown(str(a[4]))
pyautogui.keyDown('space')
pyautogui.keyDown(str(a[5]))
pyautogui.keyDown('space')
i = 0
while i != len(t):
    pyautogui.keyDown(t[i])
    i += 1
pyautogui.keyDown('enter')