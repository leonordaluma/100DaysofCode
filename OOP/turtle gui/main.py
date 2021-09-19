from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
color = ["MediumAquamarine", "LightCoral", "Tomato", "LightBlue", "MistyRose", "DarkOrange"]

def draw_shape(sides):
    shape_angle = 360 / sides
    for _ in range(sides):
        tim.right(shape_angle)
        tim.forward(100)

for n in range(3,11):
    tim.color(random.choice(color))
    draw_shape(n)

# tim.right(120)
# tim.forward(100)
# tim.right(120)
# tim.forward(100)



screen = Screen()
screen.exitonclick()