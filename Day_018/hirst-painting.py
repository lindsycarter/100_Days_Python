import random
import turtle as turtle_module


# create turtle
timmy = turtle_module.Turtle()
# set color mode in the Turtle module to RGB to use instead of the color list below
turtle_module.colormode(255)
# change the shape
timmy.shape("turtle")
# change the color
timmy.color("CadetBlue4")
# set turtle speed
timmy.speed("fastest")
# hide the turtle shape
timmy.hideturtle()

# color_list from colorgram_extract_colors.py file
color_list = [
    (208, 158, 96), (234, 213, 101), (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162), (148, 65, 83),
    (24, 40, 55), (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121), (59, 117, 93), (26, 44, 36),
    (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7), (226, 175, 167), (13, 96, 75),
    (41, 59, 99), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59)
]

# create spot painting with 10 X 10 rows of spots
# size 20
# spaced apart by 50

# set starting spot for turtle
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    timmy.dot(20, random.choice(color_list))

    timmy.forward(50)

    # start a new line
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)








# create screen object and function to exit on click
screen = turtle_module.Screen()
screen.exitonclick()