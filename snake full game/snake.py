from turtle import Turtle

STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:

    def __init__(self):
        self.snake_body=[]
        self.Create_snake()
        self.head=self.snake_body[0]

    def Create_snake(self):
        for position in STARTING_POSITION:
            self.segment(position)
            
    def segment(self,position):
        sanke_=Turtle()
        sanke_.shape("square")
        sanke_.color("#54F82F")
        sanke_.penup()
        sanke_.goto(position)
        self.snake_body.append(sanke_)
    
    def extend_snake(self):
        self.segment(self.snake_body[-1].position())
    
    def move(self):
        for snake_body_part in range(len(self.snake_body)-1,0,-1):
            x_coordinate=self.snake_body[snake_body_part-1].xcor()
            y_coordinate=self.snake_body[snake_body_part-1].ycor()
            self.snake_body[snake_body_part].goto(x_coordinate,y_coordinate)
        self.head.forward(MOVE_DISTANCE)
        # self.snake_body[0].right(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)