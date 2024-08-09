from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.screensize(800, 600)
screen.listen()

# initialise components
r_paddle = Paddle((400, 0))
l_paddle = Paddle((-400, 0))
ball = Ball()

# move the paddle up and down
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

game_over = False
while not game_over:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.distance(y=380, ) < 20 or ball.distance(y=-380) < 20:
        ball.bounce('wall')
    if ball.distance(r_paddle) < 20 or ball.distance(l_paddle) < 20:
        ball.bounce('paddle')

screen.exitonclick()
