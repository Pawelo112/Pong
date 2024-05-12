from turtle import Turtle


class Scoreboard(Turtle):
    """Keeps and displays score of two players."""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.display_score()

    def display_score(self):
        """Method that displays current score."""
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def update_left_score(self):
        """Updates the score of the left player after getting a point."""
        self.l_score += 1
        self.display_score()

    def update_right_score(self):
        """Updates the score of the right player after getting a point."""
        self.r_score += 1
        self.display_score()
