from turtle import Turtle

class Padle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.setpos(x_pos, y_pos)
    

    def go_up(self):
        self.new_y = self.ycor() + 50
        self.goto(self.xcor(), self.new_y)
    
    def go_down(self):
        self.new_y = self.ycor() - 50
        self.goto(self.xcor(), self.new_y)

