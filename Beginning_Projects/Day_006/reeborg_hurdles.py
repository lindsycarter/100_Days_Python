def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_hurdle():
    while not at_goal():
        if front_is_clear():
            move()
        else:
            turn_left()
            while wall_on_right():
                move()
            turn_right()
            move()
            turn_right()
            while front_is_clear():
                move()
            turn_left()

jump_hurdle()