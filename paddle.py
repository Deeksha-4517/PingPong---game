from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(pos)

    def up(self):
        y = self.ycor()
        self.sety(y + 20)


    def down(self):
        y = self.ycor()
        self.sety(y - 20)