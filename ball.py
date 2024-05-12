from turtle import Turtle


class Ball(Turtle):
    """Returns pong ball object."""
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """Moves the ball across the screen."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce(self):
        """Moves the ball across the screen after collision with the top or bottom wall."""
        self.y_move *= -1

    def bounce_back(self):
        """Moves the ball across the screen after collision with the paddle."""
        self.x_move *= -1

    def reset(self):
        """Resets the ball, after going out of bounds"""
        self.goto(0, 0)
        self.bounce_back()
