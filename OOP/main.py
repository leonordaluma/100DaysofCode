from turtle import Turtle, Screen

timmy = Turtle()
rafael = Turtle()
timmy.shape("turtle")
rafael.shape("turtle")
rafael.color('blue')
timmy.color('red')
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()