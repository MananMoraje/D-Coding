import turtle
import os

#  Window
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Space Invaders')

#  Borders
borderp = turtle.Turtle()
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

#  Player object
p = turtle.Turtle()
p.color("Blue")
p.shape("triangle")
p.penup()
p.speed(0)
p.setposition(0, -250)
p.setheading(90)


pm = 15

ene = turtle.Turtle()
ene.color('red')
ene.shape('square')
ene.penup()
ene.speed(0)
ene.setposition(-200, 250)

em = 2

bullet = turtle.Turtle()
bullet.hideturtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)


bulletspeed = 25
bulletstate = 'ready'


def fire():
    global bulletstate
    xx = p.xcor()
    yy = p.ycor() + 10
    bullet.setposition(xx, yy)
    bullet.showturtle()


def left():
    xx = p.xcor()
    xx -= pm
    if xx < -280:
        xx = -280
    p.setx(xx)


def right():
    xx = p.xcor()
    xx += pm
    if xx > 280:
        xx = 280
    p.setx(xx)


while True:

    wn.onkey(left(), 'a')
    wn.onkey(right(), 'd')
    wn.onkey(fire(), 'space')
    #wn.listen()

    x = ene.xcor()
    x += em
    ene.setx(x)

    if ene.xcor() > 280:
        em *= -1

        y = ene.ycor()
        y -= 40
        em *= 1
        ene.sety(y)
    if ene.xcor() < -280:
        em *= 1

        y = ene.ycor()
        y -= 40
        em *= -1
        ene.sety(y)


