import turtle
from turtle import Turtle, Screen
import random

# create turtle
timmy = Turtle()
# set color mode in the Turtle module to RGB to use instead of the color list below
turtle.colormode(255)
# change the shape
timmy.shape("turtle")
# change the color
timmy.color("CadetBlue4")
# set turtle speed
timmy.speed("fastest")


# create function to choose random RGB colors by number value
def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    new_color = (red, green, blue)
    return new_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(3)

# create screen object and function to exit on click
screen = Screen()
screen.exitonclick()
