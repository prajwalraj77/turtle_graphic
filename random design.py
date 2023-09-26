from turtle import Turtle,Screen,colormode
from random import choice, randint

turtle_1=Turtle()

# turtle_1=colormode()
colormode(255)


def new_color():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    random_color=(r,g,b)
    return random_color


direction=[0,90,180,270]

turtle_1.pensize(15)
turtle_1.speed("fastest")


for i in range(200):
    turtle_1.forward(30)
    random_movement=choice(direction)
    turtle_1.setheading(random_movement)
    turtle_1.color(new_color())



turtle_1=Screen()
turtle_1.exitonclick()