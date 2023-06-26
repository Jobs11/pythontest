import turtle
import random


def star():
    turtle.forward(200)
    turtle.right(150)
    turtle.forward(200)
    turtle.right(150)
    turtle.forward(200)
    turtle.right(150)
    turtle.forward(200)
    turtle.right(135)
    turtle.forward(180)


def tri():
    turtle.forward(200)
    turtle.right(120)
    turtle.forward(200)
    turtle.right(120)
    turtle.forward(200)


def rec():
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)


def longrec():
    for i in range(1, 5):
        if i == 1:
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
        else:
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)


def grec():
    for i in range(1, 5):
        if i == 1:
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
        elif i == 4:
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
        else:
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)


def midrec():
    for i in range(1, 5):
        if i == 1:
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
        elif i == 4:
            turtle.forward(50)
            turtle.right(-90)
            turtle.forward(50)
            turtle.right(-90)
            turtle.forward(50)
            turtle.right(-90)
            turtle.forward(50)
        else:
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)


def midrec90():
    for i in range(1, 5):
        if i == 1:
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(180)
        else:
            turtle.forward(100)
            turtle.right(-90)
            turtle.forward(50)
            turtle.right(-90)
            turtle.forward(50)
            turtle.right(-90)
            turtle.forward(50)
            turtle.right(-90)


def screenLeftClick(x, y):
    global r, g, b, angle, pSize
    r = random.random()
    g = random.random()
    b = random.random()
    #    tSize = random.randrange(1, 10)
    pSize = random.randrange(1, 20)
    stype = random.randrange(1, 4)

    # turtle.shapesize(tSize)
    turtle.pensize(pSize)
    turtle.pencolor((r, g, b))
    turtle.goto(x, y)
    print("도형: ", stype)
    turtle.pendown()
    if stype == 1:
        midrec90()
        turtle.right(-90)
    elif stype == 2:
        grec()
        turtle.right(180)
    elif stype == 3:
        midrec()

    turtle.penup()


s = turtle.Screen()
img1 = "img/한글.gif"
s.addshape(img1)

turtle.shape(img1)
turtle.resizemode("user")
turtle.penup()
turtle.shapesize(1)
turtle.speed(30)
turtle.onscreenclick(screenLeftClick, 1)
turtle.done()
