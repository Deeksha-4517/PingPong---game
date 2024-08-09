from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)


    def move(self):
        self.x = self.xcor() + 10
        self.y = self.ycor() + 10
        self.goto(x=self.x, y=self.y)

    def bounce(self, object):
        if object == 'wall':
            self.y *= -1
        else:
            self.x *= -1