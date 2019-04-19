import turtle
import time

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Sliding Square')

i = 0
while i != 100:
    time.sleep(0.05)

    sq1 = turtle.Turtle()
    sq1.color('red')
    sq1.shape('square')
    sq1.speed(0)
    sq1.penup()

    i += 1
    x1 = sq1.xcor()
    x1 += 1
    if x1 > 280:
        x1 *= -1
    elif x1 < -280:
        x1 *= 1
wn.bye()
