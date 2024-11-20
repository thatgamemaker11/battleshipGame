from turtle import *
def peg(col,row,hit):


    if col == "a":
        pegx = -200
    elif col == "b":
        pegx = -110
    elif col == "c":
        pegx = -20
    elif col == "d":
        pegx = 70
    else:
        pegx = 160
#============================
    if row == 1:
        pegy = 180
    elif row == 2:
        pegy = 90
    elif row == 3:
        pegy = 0
    elif row == 4:
        pegy = -90
    else:
        pegy = -180

#==========================
    if hit == 1:
        fillcolor("red")
        pencolor("red")
    elif hit == 2:
        fillcolor("white")
        pencolor("white")
    else:
        fillcolor("black")
        pencolor("black")
    penup()
    goto(pegx,pegy)
    pendown()
    begin_fill()
    circle(20,360)
    end_fill()

