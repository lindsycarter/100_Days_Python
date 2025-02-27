# 1. Move the turtle with keypress
# 2. Create and move the cars
# 3. Detect collision with car
# 4. Detect when turtle reaches the other side
# 5. Create a scoreboard


import time
from turtle import Screen
from player_manager import Player
from car_manager import CarManager
from scoreboard_manager import Scoreboard


# Do I need to update to python 3.8?

# set screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# set player
player = Player()

# set car manager
car_manager = CarManager()

# set scoreboard
scoreboard = Scoreboard()

# set listener and key bindings
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect a successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.increase_level()


# END OF PROGRAM

# exit on click
screen.exitonclick()
