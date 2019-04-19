import pyautogui
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
i = random.randint(0, len(letters))
ii = random.randint(0, len(numbers))

while True:
    pyautogui.keyDown('ctrl' + i)
    pyautogui.keyDown('ctrl' + 'shift' + i)
    pyautogui.keyDown('backspace')
    pyautogui.keyDown(letters[i])
    pyautogui.keyDown(numbers[ii])