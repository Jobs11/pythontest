import turtle

# 초기화
window = turtle.Screen()
window.title("세모 도형 옮기기")
window.bgcolor("white")

pen = turtle.Turtle()
pen.speed(1)  # 그리는 속도 설정


# 세모 그리기
def draw_triangle():
    for _ in range(3):
        pen.forward(100)
        pen.right(120)


draw_triangle()

# 도형 이동
pen.penup()  # 펜 들기
pen.goto(200, 200)  # 새로운 위치로 이동
pen.pendown()  # 펜 내리기

draw_triangle()


# 옮기기
def move_triangle(x, y):
    pen.penup()  # 펜 들기
    pen.goto(x, y)  # 새로운 위치로 이동
    pen.pendown()  # 펜 내리기


move_triangle(-200, -200)  # 새로운 위치로 이동

draw_triangle()

turtle.done()
