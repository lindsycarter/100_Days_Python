from turtle import Turtle, Screen

# create turtle
timmy = Turtle()
# change the shape
timmy.shape("turtle")
# change the color
timmy.color("CadetBlue4")

# Draw a Dashed Line
for _ in range(50):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

# create screen object and function to exit on click
screen = Screen()
screen.exitonclick()
