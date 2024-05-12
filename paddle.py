from turtle import Turtle


class Paddle(Turtle):
    """Paddle that moves up and down.
    By default, the paddle is created on the right edge of the screen - to make paddle
    on the left type - left."""

    def __init__(self, side):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5.0, stretch_len=1.0)
        self.color("white")

        if side != "left":
            self.right_side()
        else:
            self.left_side()

    def left_side(self):
        """Moves the paddle to the left side of the screen."""
        self.goto(x=-350, y=0)

    def right_side(self):
        """Moves the paddle to the right side of the screen."""
        self.goto(x=350, y=0)

    def up(self):
        """Method that moves paddle up 20 pixels"""
        self.goto(x=self.xcor(), y=self.ycor() + 25)

    def down(self):
        """Method that moves paddle down 20 pixels"""
        self.goto(x=self.xcor(), y=self.ycor() - 25)
