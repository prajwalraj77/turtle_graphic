from turtle import  Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.all_car=[]
        self.car_speed=MOVE_INCREMENT

    def create_car(self):
        random_car=random.randint(1,6)
        if random_car==1:
            car=Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car_distance_y=random.randint(-250,250)
            car.goto(300,car_distance_y)
            self.all_car.append(car)

    def move_car(self):
        for car in self.all_car:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed +=MOVE_INCREMENT
