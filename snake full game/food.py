from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.refresh_food()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        

    def refresh_food(self):
        x_direction=random.randint(-320,320)
        y_direction=random.randint(-320,320)
        self.goto(x=x_direction,y=y_direction)