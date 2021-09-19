from turtle import Turtle, Screen
from random import randint

tim = Turtle()
screen = Screen()

def draw_shape(shape_angle, sides):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    screen.colormode(255)
    tim.pencolor(r,g,b)
    for _ in range(sides):
        tim.right(shape_angle)
        tim.forward(100)

draw_shape(120,3)
draw_shape(90,4)
draw_shape(72,5)
draw_shape(60,6)
draw_shape(51.42, 7)
draw_shape(45, 8)
draw_shape(40, 9)
draw_shape(36, 10)

# tim.right(120)
# tim.forward(100)
# tim.right(120)
# tim.forward(100)



screen = Screen()
screen.exitonclick()