# To do items:
# 1. Create the Screen
# 2. Create and move a paddle
# 3. Create another paddle and make it move
# 4. Create the ball and make it move on its own
# 5. Detect collision with wall and bounce
# 6. Detect collision with paddle and bounce
# 7. Detect when paddle misses
# 8. Keep score


from turtle import Screen
from paddle_class import Paddle
from ball_class import Ball
from scoreboard_class import Scoreboard
import time

# Create turtles
# set screen
screen = Screen()
screen.screensize(canvwidth=800, canvheight=600, bg="black")
screen.title("Pong")
# hide paddle so you don't see it float across the screen since they all start at the 0, 0 point
screen.tracer(0)

# set paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# set ball
ball = Ball()

# set scoreboard
scoreboard = Scoreboard()

# set listener and key bindings
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()

    # Detect collision with wall
    # when ball is ycor > 300 (or > -300)
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle missed
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# END PROGRAM
# Exit the screen on click
screen.exitonclick()
