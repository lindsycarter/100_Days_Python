from turtle import Turtle, Screen

# create objects
timmy = Turtle()
screen = Screen()


# move forward function
def move_forward():
    timmy.forward(10)


# move backwards function
def move_backwards():
    timmy.backward(10)


# turn left function
def turn_counter_clockwise():
    timmy.left(10)


# turn clockwise function
def turn_clockwise():
    timmy.right(10)


def clear_drawing():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


# start screen listening
screen.listen()

# function as input
# assign keys to their functions
# 'w' to move forwards
screen.onkey(move_forward, "w")
# 's' to move backwards
screen.onkey(move_backwards, "s")
# 'a' to turn counter-clockwise
screen.onkey(turn_counter_clockwise, "a")
# 'd' to turn clockwise
screen.onkey(turn_clockwise, "d")
# 'c' to clear the drawing
screen.onkey(clear_drawing, "c")

# exit on click
screen.exitonclick()
