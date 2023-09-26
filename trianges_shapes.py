from turtle import Turtle,Screen
from random import choice

turtle_1=Turtle()

def no(num_side):
    
    for i in range(num_side):
        angle =360/num_side
        turtle_1.forward(100)
        turtle_1.right(angle)


colors = ["red", "green", "blue", "orange", "purple", "yellow"]


for i in range(3,9):
    turtle_1.color( choice(colors))
    no(i)
    

turtle_1=Screen()
turtle_1.exitonclick()

