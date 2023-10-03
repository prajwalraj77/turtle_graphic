from turtle import Turtle, Screen

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game by PRAJWAL")
screen.tracer(0)

paddle=Turtle("square")
paddle.penup()
paddle.color("yellow")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.goto(350,0)

def up():
    y_cor=paddle.ycor()+20
    paddle.goto(paddle.xcor(),y_cor)
def down():
    y_cor = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), y_cor)


screen.listen()
screen.onkey(key="Up",fun=up)
screen.onkey(key="Down",fun=down)

game_is_on=True
while game_is_on:
    screen.update()


screen.exitonclick()