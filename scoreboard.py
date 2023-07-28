from turtle import Turtle
# Constants
TOP_CENTER_X = 0
TOP_CENTER_Y = 270
ALIGNMENT = "center"
FONT = ("Harrington", 22, "normal")


class Scoreboard(Turtle):  # Inheriting from the Turtle class
    def __init__(self):
        super().__init__()
        self.score = 0  # Setting up our scoreboard
        self.color("white")
        self.penup()
        self.goto(TOP_CENTER_X, TOP_CENTER_Y)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):  # Updating the scoreboard
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):  # Increasing the score
        self.score += 1
        self.clear()  # Removing the previous number
        self.update_scoreboard()

    def gameover(self):  # Gameover message
        self.goto(TOP_CENTER_X, TOP_CENTER_X)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)