from turtle import Turtle, Screen
import random

# create objects
# create screen
screen = Screen()
# set up screen with specific dimensions 500px wide 400px tall
screen.setup(width=500, height=400)
# add input pop up
user_choice = screen.textinput(title='Make your choice.', prompt="Which turtle will win the race, "
                                                                 "please choose a color: ")

# create lists and variables
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False

# create 6 turtle objects
for turtle_index in range(0, 6):
    # set shape
    new_turtle = Turtle(shape="turtle")
    # set colors from the list
    new_turtle.color(colors[turtle_index])
    # stop drawing
    new_turtle.penup()
    # go to starting line
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    # append to all_turtle list
    all_turtles.append(new_turtle)

# wait to start race until user makes choice
if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# exit on screen click
screen.exitonclick()
