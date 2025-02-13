from turtle import Turtle, Screen

# create turtle
timmy = Turtle()
# change the shape
timmy.shape("turtle")
# change the color
timmy.color("CadetBlue4")

# Draw a Square
for _ in range(4):
    timmy.forward(100)
    timmy.left(90)
# return to original facing
timmy.setheading(0)

# create screen object and function to exit on click
screen = Screen()
screen.exitonclick()
