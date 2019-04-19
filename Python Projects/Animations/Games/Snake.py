
import turtle as t
import random as r
import time

wn = t.Screen()
wn.bgcolor('black')
wn.title('Snake')

#  Borders

borderp = t.Turtle()
borderp.speed(0)
borderp.color('white')
borderp.penup()
borderp.setposition(-300, -300)
borderp.pendown()
borderp.pensize(3)
for side in range(4):
    borderp.fd(600)
    borderp.lt(90)
borderp.hideturtle()

#  Snake

s = t.Turtle()
s.color('red')
s.shape('square')
f = 1
s.shapesize(1, f)
s.speed(0)

speed = 20


def left():
    x = s.xcor()
    x -= speed


def right():
    x = s.xcor()
    x += speed


def up():
    y = s.ycor()
    y += speed


def down():
    y = s.ycor()
    y -= speed


#  End Causes
    #  a. Crash into barrier
    #  b. Crash into itself

#  Crash into barrier
if s.xcor() >= 300 or s.xcor() <= -300 or s.ycor() >= 300 or s.ycor() <= -300:
    wn.bye()
    print('You crashed into the barrier')
    print('GAME OVER')

#  Crash into itself
print('')
#  Food
    #  a. Position
    #  b. Add to snake length

#  Position

fx = r.randint(-300, 300)
fy = r.randint(-300, 300)
food = t.Turtle()
food.setposition(fx, fy)
food.shape('square')
food.shapesize(1, 1)
food.speed(0)
food.color('blue')
food.hideturtle()

#  Add to snake length

if s.xcor == food.xcor and s.ycor() == food.ycor():
    f += 1
wn.listen()
wn.onkeypress(left(), 'Left')
wn.onkeypress(right(), 'Right')
wn.onkeypress(up(), 'Up')
wn.onkeypress(down(), 'Down')
wn.update()
wn.mainloop()
t.done()
