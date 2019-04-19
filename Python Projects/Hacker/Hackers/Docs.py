import pyautogui
import random
import time

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
a = 0

while a != 10000:
    a += 1
    i = random.randint(0, len(letters))
    ii = random.randint(0, len(numbers))
    time.sleep(0.01)
    pyautogui.keyDown(letters[i])
    time.sleep(0.01)
    pyautogui.keyDown(numbers[ii])

