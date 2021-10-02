from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
def move_forwards():
    tim.fd(50)

def move_backwards():
    tim.bk(50)

def turn_left():
    new_heading = tim.heading() + 10
    tim.seth(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.seth(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()