from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400) # dialog box size

colour_of_turtle=["red", "green", "blue", "gray", "orange", "purple", "pink", ]

user_bet=screen.textinput(title="who will win the race",prompt="bet on turtle colour") #input dialog box


y_postion=[-100,-70,-40,-10,20,50]

all_turtle=[]

for i in range(6):
    turtle_1=Turtle(shape="turtle")
    turtle_1.color(colour_of_turtle[i])
    turtle_1.penup()
    turtle_1.goto(x=-230,y=y_postion[-i])
    all_turtle.append(turtle_1)
flag=False

if user_bet:
    flag=True

while flag:
    for i in all_turtle:
        if i.xcor()>230: #x cocoordinate 
            winner=i.pencolor()
            if user_bet==winner:
                print(" ur win")
            else:
                print("u lost")
            flag=False
        turtle_s=random.randint(0,10)
        i.forward(turtle_s)


screen.exitonclick()