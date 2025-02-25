from turtle import Turtle
import random


# food class will inherit from the Turtle class
class Food(Turtle):

    def __init__(self):
        # initiate super class when you are using class inheritance
        super().__init__()
        # render itself as a small circle on the screen
        self.shape("circle")
        self.penup()
        # turtles are default 20x20, stretching by 1/2 makes the circle 10x10
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    # every time the snake touches it, it moves to another random location
    def refresh(self):

        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)
