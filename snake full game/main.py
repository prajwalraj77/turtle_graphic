from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time



''' screen type'''
screen=Screen()
screen.setup(width=700,height=700)
screen.bgcolor("black")                       
screen.title("classical snake game by Prajwal")
screen.tracer(0)

""" snake creation"""
snake=Snake()

""" food creation"""
food=Food()

'''score board'''
score=Score()

'''snake movement'''
screen.listen() 
screen.onkey(key="w",fun=snake.up)
screen.onkey(key="s",fun=snake.down)
screen.onkey(key="d",fun=snake.right)
screen.onkey(key="a",fun=snake.left)



GAME_IS_ON=True

while GAME_IS_ON:
    screen.update()
    time.sleep(0.1)
    snake.move()
    

    #Detect collision with food
    if snake.head.distance(food)<15:
        food.refresh_food()
        score.score_count()
        snake.extend_snake()
    
     #Detect collision with Wall
    if snake.head.xcor() > 340 or snake.head.xcor() < -340 or snake.head.ycor() > 340 or snake.head.ycor()< -340:
        GAME_IS_ON=False
        score.game_over()

    #Detect collision with Snake tail
    for body in snake.snake_body[1:]:
        if snake.head.distance(body) < 10:
            GAME_IS_ON=False
            score.game_over()
            


screen.exitonclick()