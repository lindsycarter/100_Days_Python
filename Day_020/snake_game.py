# 1. Create a snake body
# 2. Move the snake
# 3. Control the snake (keyboard arrows)
# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall - game over
# 7. Detect collision with tail - game over

from turtle import Turtle, Screen
from snake import Snake
import time

# Create and set up objects
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# turn off tracer method
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

# close screen on click
screen.exitonclick()
