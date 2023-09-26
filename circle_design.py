from turtle import Turtle,Screen,colormode
from random import choice, randint
turtle_1=Turtle()
turtle_1.speed(0)
colormode(255)


def new_colour():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    return r,g,b
     


for i in range(72):
    turtle_1.color(new_colour())
    turtle_1.left(5)
    turtle_1.circle(100)

turtle_1=Screen()
turtle_1.exitonclick()