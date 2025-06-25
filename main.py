from turtle import  Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Creates the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

ball = Ball()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
# paddle.penup()
# paddle.shape("square")
# paddle.shapesize(stretch_len=1,stretch_wid=5)
# paddle.goto(350,0)
# paddle.color("white")

score = Scoreboard()

screen.listen()

screen.onkeypress(fun=r_paddle.go_down,key="Down")
screen.onkeypress(fun=r_paddle.go_up,key="Up")

screen.onkeypress(fun=l_paddle.go_down,key="s")
screen.onkeypress(fun=l_paddle.go_up,key="w")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    #Detect collision with wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()
        
    # Detect collision with paddle
    elif ball.xcor()>320 and ball.distance(r_paddle) < 50 or ball.xcor()<-320 and ball.distance(l_paddle) <50:
        ball.bounce_x()

    # Detect R paddle misses the ball
    if ball.xcor() > 380:
        ball.refresh()
        score.l_point()
    
    # Detect L paddle misses the ball
    elif ball.xcor() < -380:
        ball.refresh()
        score.r_point()

screen.exitonclick()