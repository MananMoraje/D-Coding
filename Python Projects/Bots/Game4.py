from PIL import ImageGrab, ImageOps
import pyautogui

currentGrid = [0, 0, 0, 0,
               0, 0, 0, 0,
               0, 0, 0, 0,
               0, 0, 0, 0]


class Cords:
    cord11 = (170, 270)
    cord12 = (270, 270)
    cord13 = (370, 270)
    cord14 = (470, 270)
    cord21 = (170, 370)
    cord22 = (270, 370)
    cord23 = (370, 370)
    cord24 = (470, 370)
    cord31 = (170, 480)
    cord32 = (270, 480)
    cord33 = (370, 480)
    cord34 = (470, 480)
    cord41 = (170, 590)
    cord42 = (270, 590)
    cord43 = (370, 590)
    cord44 = (470, 590)

    cordArray = [cord11, cord12, cord13, cord14,
                 cord21, cord22, cord23, cord24,
                 cord31, cord32, cord33, cord34,
                 cord41, cord42, cord43, cord44]


class Values:
    empty = 195
    two = 229
    four = 225
    eight = 190
    sixteen = 172
    thirtyTwo = 157
    sixtyFour = 135
    oneTwentyEight = 205
    twoFiftySix = 201
    fiveOneTwo = 197
    oneZeroTwoFour = 193
    twoZeroFourEight = 189

    valueArray = [empty, two, four, eight, sixteen, thirtyTwo, sixtyFour
        , oneTwentyEight, twoFiftySix, fiveOneTwo, oneZeroTwoFour,
                  twoZeroFourEight]


def getgrid():
    image = ImageGrab.grab()
    gi = ImageOps.grayscale(image)
    j = 0
    for index, cord, j in enumerate(Cords.cordArray):
        pixel = gi.getpixel(cord)
        pos = Values.valueArray.index(pixel[j], pixel[j + 1])
        j += 1
        if pos == 0:
            currentGrid[index] = 0
        else:
            currentGrid[index] = pow(2, pos)


def printgrid(grid):
    for i in range(16):
        if i % 4 == 0:
            print("[ " + str(grid[i]) + " " + str(grid[i+1]) + " " + str(grid[i+2]) + " " + str(grid[i+3]) + " ]")


getgrid()
printgrid(currentGrid)
