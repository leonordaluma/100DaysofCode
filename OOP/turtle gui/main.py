import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


color = ["MediumAquamarine", "LightCoral", "Tomato", "LightBlue", "MistyRose","DarkOliveGreen", "LightGreen", "SlateBlue", "RoyalBlue"]
directions = [0,90,180,270]
tim.speed('fastest')
tim.pensize(10)

for _ in range(250):
    tim.color(random_color())
    direction = random.choice(directions)
    tim.seth(direction)
    tim.fd(25)

screen = Screen()
screen.exitonclick()