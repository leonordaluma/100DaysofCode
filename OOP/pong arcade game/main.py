from turtle import Screen
from padle import Padle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

padle = Padle()
screen.listen()

screen.onkey(padle.go_up, "Up")
screen.onkey(padle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()




screen.exitonclick()