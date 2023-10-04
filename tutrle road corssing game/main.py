import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

palyer=Player()
screen.onkeypress(key='Up', fun=palyer.up)
screen.onkeypress(key='Down', fun=palyer.down)
screen.onkeypress(key='Left', fun=palyer.left)
screen.onkeypress(key='Right', fun=palyer.right)


car_manager=CarManager()

score=Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    car_manager.create_car()
    car_manager.move_car()

    # car collision
    for car in car_manager.all_car:
        if car.distance(palyer) <20:
            game_is_on=False
            score.game_over()



    #level up on crossing the road

    if palyer.finish_line():
        palyer.start_line()
        car_manager.level_up()
        score.clear()
        score.increse_level()

screen.exitonclick()
