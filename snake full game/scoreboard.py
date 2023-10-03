from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial",24,'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.color("red")
        self.penup()
        self.goto(x=0,y=310)
        self.update_score_board()

    
    def update_score_board(self):
        self.write(f"SCORE ={self.score} ",align=ALIGMENT,font=FONT)

    def score_count(self):
        self.score += 1
        self.clear()
        self.update_score_board()
    
    def game_over(self):
        self.goto(0,0)
        self.write("game over ",align=ALIGMENT,font=FONT)
        


    