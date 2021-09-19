from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
color = ["MediumAquamarine", "LightCoral", "Tomato", "LightBlue", "MistyRose","DarkOliveGreen", "LightGreen", "SlateBlue", "RoyalBlue"]
directions = [0,90,180,270]
tim.speed('fastest')
tim.pensize(10)

for _ in range(250):
    tim.color(random.choice(color))
    direction = random.choice(directions)
    tim.seth(direction)
    tim.fd(25)

screen = Screen()
screen.exitonclick()