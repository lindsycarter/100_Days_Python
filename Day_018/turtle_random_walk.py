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
# set pen size
timmy.pensize(5)


# create function to choose random RGB colors by number value
def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    new_color = (red, green, blue)
    return new_color

# create list of colors
# uncomment the color list when you want to define specific, named color
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#           "SeaGreen"]
# create list of directions
directions = [0, 90, 180, 270]

for rand_walk in range(1, 1001):
    timmy.color(random_color())
    timmy.setheading(random.choice(directions))
    timmy.speed('fastest')
    timmy.forward(20)

# create screen object and function to exit on click
screen = Screen()
screen.exitonclick()
