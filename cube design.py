from turtle import Turtle, Screen 

turlte_1=Turtle()
turlte_1.color("red" )
turlte_1.shape("turtle")

turlte_2=Turtle()
turlte_2.color("green")
turlte_2.shape("turtle")

turlte_3=Turtle()
turlte_3.color("blue")
turlte_3.shape("turtle")

turlte_4=Turtle()
turlte_4.color("violet")
turlte_4.shape("turtle")

for i in range(4):
        turlte_1.forward(100)
        turlte_1.left(90)


for i in range(4):
    turlte_2.forward(100)
    turlte_2.right(90)

for i in range(4):
        turlte_3.bk(100)
        turlte_3.left(90)


for i in range(4):
    turlte_4.bk(100)
    turlte_4.right(90)




small_turlte=Screen()
small_turlte.exitonclick()