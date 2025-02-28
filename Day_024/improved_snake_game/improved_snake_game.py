# 1. Create a snake body
# 2. Move the snake
# 3. Control the snake (keyboard arrows)
# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall - game over
# 7. Detect collision with tail - game over

from turtle import Screen
from snake_manager import Snake
from Day_024.improved_snake_game.improved_snake_game import Food
from scoreboard_manager import Scoreboard
import time

# Create and set up objects
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# turn off tracer method
screen.tracer(0)

# create turtles
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# start listening for assigned keystrokes
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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        # food should go to a new random location
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# close screen on click
screen.exitonclick()
