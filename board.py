from turtle import *
def board():
    penup()
    pensize(5)
    speed(0)
    back(225)
    left(90)
    forward(225)
    right(90)
    for i in range(5):

        for i in range(5):
            fillcolor("blue")
            begin_fill()
            pendown()
            forward(90)
            right(90)
            forward(90)
            right(90)
            forward(90)
            right(90)
            forward(90)
            right(90)
            end_fill()

            forward(90)
        penup()
        right(90)
        forward(90)
        right(90)
        forward(90*5)
        setheading(0)

    goto(-225,225)
    #write("abcde")
    write("A   B   C   D   E", align="left", font=("Arial", 48, "bold"))

    back(70)#how close numbers are to the board

    right(90)
    forward(90)
    write("1", align="left", font=("Arial", 48, "bold"))
    forward(90)
    write("2", align="left", font=("Arial", 48, "bold"))
    forward(90)
    write("3", align="left", font=("Arial", 48, "bold"))
    forward(90)
    write("4", align="left", font=("Arial", 48, "bold"))
    forward(90)
    write("5", align="left", font=("Arial", 48, "bold"))
