from PIL import ImageGrab, ImageOps
import pyautogui


def vision():
    image =ImageGrab.grab()
    gray = ImageOps.grayscale(image)