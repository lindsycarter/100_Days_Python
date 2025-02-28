from turtle import Turtle

# create constants
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


# scoreboard class will inherit from the Turtle class
class Scoreboard(Turtle):

    def __init__(self):
        # initiate super class when you are using class inheritance
        super().__init__()

        self.score = 0
        with open("highest_score.txt") as highest_score:
            self.high_score = int(highest_score.read())

        self.color("white")
        self.penup()
        # move it to the top of the screen
        self.goto(0, 260)

        # hide the turtle
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}. High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("highest_score.txt", mode="w") as highest_score:
            highest_score.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # Removed game_over function and added the above reset function
    #    def game_over(self):
    #        self.goto(0, 0)
    #        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
