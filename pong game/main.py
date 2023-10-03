from turtle import Turtle, Screen
from paddel import Paddle
from ball import Ball
from score_board import Score
import time
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game by PRAJWAL")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

screen.listen()

screen.onkeypress(key="Up",fun=r_paddle.up)
screen.onkeypress(key="Down",fun=r_paddle.down)

screen.onkeypress(key="w",fun=l_paddle.up)
screen.onkeypress(key="s",fun=l_paddle.down)

ball=Ball()

score=Score()

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    #detect wall collison
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect paddel collison
    if ball.distance(r_paddle) <50 and ball.xcor()>320 or ball.distance(l_paddle) <50 and ball.xcor() <-320:
        ball.bounce_x()


    if ball.xcor() >380 :
        ball.restart()
        score.clear()
        score.l_score_count()

    if ball.xcor() < -380:
        ball.restart()
        score.clear()
        score.r_score_count()

screen.exitonclick()