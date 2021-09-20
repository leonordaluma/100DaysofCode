import turtle as t
import random

tim = t.Turtle()
tim.speed('fastest')
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


for _ in range(80):
    tim.color(random_color())
    tim.circle(100)
    current_heading = tim.heading()
    tim.seth(current_heading + 5)

    

screen = t.Screen()
screen.exitonclick()