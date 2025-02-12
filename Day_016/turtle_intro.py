import turtle
from turtle import Turtle, Screen

# construct new object
timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkCyan")
print(timmy)

timmy.forward(100)

new_screen = Screen()
print(new_screen.canvheight)
print(new_screen.canvwidth)

# will exit the screen on click
new_screen.exitonclick()