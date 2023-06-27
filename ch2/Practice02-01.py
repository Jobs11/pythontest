import turtle
import random


def screenLeftClick(x, y):
    global r, g, b, angle, pSize
    r = random.random()
    g = random.random()
    b = random.random()
    angle = random.randrange(1, 360)
    tSize = random.randrange(1, 10)
    pSize = random.randrange(1, 20)

    turtle.shapesize(tSize)
    turtle.pensize(tSize)
    turtle.right(angle)
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)


def screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x, y)


## 변수 선언 부분 ##
pSize = 10
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title("거북이로 그림 그리기")
turtle.shape("turtle")

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
