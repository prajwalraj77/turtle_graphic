# import  colorgram
# colors = colorgram.extract('new_image.webp', 20)

# new_colour=[]
# for i in colors:
#     r=i.rgb.r
#     g=i.rgb.g
#     b=i.rgb.b
#     rgb=(r,g,b)
#     new_colour.append(rgb)
# print((new_colour))

from turtle import Turtle,Screen ,colormode
from random import randint,choice
colormode(255)

turtle_1=Turtle()
turtle_1.speed(0)
turtle_1.penup()

new_colour=[(241, 236, 227), (236, 246, 239), (247, 236, 240), (197, 160, 125), (136, 83, 58), (12, 24, 14), (234, 241, 246), (53, 42, 23), (220, 205, 131), (137, 177, 152), (43, 112, 139), (65, 114, 86), (128, 172, 188), (200, 136, 146), (215, 85, 62), (144, 31, 18), (138, 69, 79), (163, 144, 68), (201, 85, 99), (230, 173, 163)]

turtle_1.setheading(225)
turtle_1.forward(300)
turtle_1.setheading(0)
dots=100

def horizontal():
    for i in range(1,dots+1):
        turtle_1.dot(20,choice(new_colour))
        turtle_1.forward(50)
        if i%10==0:
            turtle_1.setheading(90)
            turtle_1.forward(50)
            turtle_1.setheading(180)
            turtle_1.forward(500)
            turtle_1.setheading(0)

horizontal()

turtle_1=Screen()
turtle_1.exitonclick()


