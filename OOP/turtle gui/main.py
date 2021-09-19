from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("SeaGreen2")
# def turn_right():
#     tim.right(90)
#     tim.forward(100)

# turn_right()
# turn_right()
# turn_right()
# turn_right()

for _ in range(4):
    tim.right(90)
    tim.forward(100)



screen = Screen()
screen.exitonclick()