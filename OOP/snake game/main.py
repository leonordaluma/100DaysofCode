from turtle import Turtle, Screen, width

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
tim = Turtle(shape="square")
tim.color("white")
tom = Turtle(shape="square")
tom.color("white")
tom.goto(x=-20, y=0)
tam = Turtle(shape="square")
tam.color("white")
tam.goto(x=-40, y=0)

screen.exitonclick()