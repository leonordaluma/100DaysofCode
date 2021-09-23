#pip install colorgram.py
import colorgram
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
rgb_colors = [(243, 242, 239), (99, 6, 51), (172, 158, 33), (75, 94, 172), (232, 209, 73), (10, 35, 127), (212, 91, 34), (177, 104, 155), (104, 122, 210), (25, 95, 40), (243, 237, 240), (33, 103, 48), (112, 130, 212), (233, 236, 245)]
number_of_dots = 100

tim.seth(225)
tim.fd(300)
for dot_count in range(1,number_of_dots):
    tim.seth(0)
    tim.dot(20, random.choice(rgb_colors))
    tim.fd(50)

    if dot_count % 10 == 0:
        tim.seth(90)
        tim.fd(50)
        tim.seth(180)
        tim.fd(500)




screen = t.Screen()
screen.exitonclick()

