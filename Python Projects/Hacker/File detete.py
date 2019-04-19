import logging, os

folderPath = input('Folder path:    ')
folderContent = []

os.access(folderPath, os.F_OK)
if not os.F_OK:
    print('Folder not valid. Please check your path')
    print(folderPath)

"""
var x = 300;
var y = 300;
var s = 200;
draw = function() {
    background(255, 255, 255);
    fill(36, 157, 222, 180);
    triangle(x - 200, x + 100 - 100, x, y - 200, x - s + 100, y);

    while(x !== 600 && y !== 600){
            y ++;
            x ++;
            s ++;
    }

    if(x === 600 || y === 600){
        x -= 2;
        y -= 3;
    }
    if(x < 0 || y < 0){
        x ++;
        y += 2;
    }
    if(s === 300){
        s -= 1;
    }
};

"""