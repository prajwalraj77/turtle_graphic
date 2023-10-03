from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("pink")
        self.speed(1)
        self.penup()
        self.x_move= 10
        self.y_move = 10
        self.ball_speed=0.1

    def move(self):
        x_pos=self.xcor() + self.x_move
        y_pos=self.ycor() + self.y_move
        self.goto(x_pos,y_pos)

    def bounce_y(self):
        self.y_move *= -1
        self.ball_speed *= 0.9
    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *=0.9

    def restart(self):
        self.goto(0,0)
        self.bounce_x()
        self.ball_speed =0.1
