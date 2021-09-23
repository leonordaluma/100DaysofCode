#pip install colorgram.py
import colorgram
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()


rgb_colors = []
colors = colorgram.extract('image.jpg', 14)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# tim.dot(20, random.choice(rgb_colors))


# screen = t.Screen()
# screen.exitonclick()

