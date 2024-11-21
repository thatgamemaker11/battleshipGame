from turtle import *

def win():
    goto(0,0)
    setheading(0)
    speed(0)
    pencolor("green")
    right(90)
    forward(200)
    left(90)
    begin_fill()
    fillcolor("green")
    pencolor("green")
    circle(200,360)
    end_fill()


    left(90)
    forward(200)
    right(90)
    back(100)
    pencolor("black")
    write("You Win!!!!", font=("Verdana",30, "normal"))


    input()
def lose():
    goto(0,0)
    setheading(0)
    speed(0)
    pencolor("red")
    right(90)
    forward(200)
    left(90)
    begin_fill()
    fillcolor("red")
    pencolor("red")
    circle(200,360)
    end_fill()


    left(90)
    forward(200)
    right(90)
    back(100)
    pencolor("black")
    write("You Lose :(", font=("Verdana",30, "normal"))

    input()