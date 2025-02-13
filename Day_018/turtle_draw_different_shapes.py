from turtle import Turtle, Screen
import random

# create turtle
timmy = Turtle()
# change the shape
timmy.shape("turtle")
# change the color
timmy.color("CadetBlue4")

# create list of colors
colors = ["dark green", "lime green", "medium aquamarine", "dark slate gray", "light sea green", "cyan", "steel blue",
          "blue"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.left(angle)


for shape_side_n in range(3, 11):
    # choose a random color from the list for each shape
    timmy.color(random.choice(colors))
    draw_shape(shape_side_n)


# create screen object and function to exit on click
screen = Screen()
screen.exitonclick()
