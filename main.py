from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.title("Pawelo Pong game!")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Creating two paddles
left_paddle = Paddle("left")
right_paddle = Paddle("right")

# Creating a ball
ball = Ball()

# Creating a scoreboard
scoreboard = Scoreboard()

# Detecting keyboard inputs
screen.listen()
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

sleep_value = 0.07
game_is_on = True
top_collision = False
while game_is_on:
    # Refreshing the screen to maintain the fluid animation.
    time.sleep(sleep_value)
    screen.update()

    # Detecting collision with the top and bottom wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detecting collision with the paddle.
    if (ball.xcor() > 335 and ball.distance(right_paddle) < 55 and ball.x_move > 0) or (ball.xcor() < -335 and
                                                                                        ball.distance(
                                                                                            left_paddle) < 55 and ball.x_move < 0):
        ball.bounce_back()
        # Increasing the speed after hitting the paddle
        sleep_value *= 0.9

    # Detecting going out of bounds
    if ball.xcor() > 380:
        ball.reset()
        sleep_value = 0.07
        scoreboard.update_left_score()

    if ball.xcor() < -380:
        ball.reset()
        sleep_value = 0.07
        scoreboard.update_right_score()

    ball.move()

screen.exitonclick()
