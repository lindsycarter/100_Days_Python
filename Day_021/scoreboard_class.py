from turtle import Turtle

# create constants
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


# scoreboard class will inherit from the Turtle class
class Scoreboard(Turtle):

    def __init__(self):
        # initiate super class when you are using class inheritance
        super().__init__()
        self.color("white")
        self.penup()
        # move it to the top of the screen
        self.goto(0, 260)
        self.score = 0
        # hide the turtle
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
