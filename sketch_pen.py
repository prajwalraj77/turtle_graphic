from turtle import Screen,Turtle

turtle_1=Turtle()
screen_=Screen()

def forw():
    turtle_1.forward(10)
def backw():
    turtle_1.backward(10)
def lef():
    turtle_1.left(10)
    
def reg():
    turtle_1.right(10)
def cl():
    turtle_1.clear()
def re():
    turtle_1.reset()


screen_.listen()
    
screen_.onkey(key="w",fun=forw)
screen_.onkey(key="s",fun=backw)
screen_.onkey(key="a",fun=lef)  
screen_.onkey(key="d",fun=reg)
screen_.onkey(key="c",fun=cl)
screen_.onkey(key="r",fun=re)


screen_.exitonclick()