from turtle import *
def peg(col,row,hit):


    if col == 1:
        pegx = -200
    elif col == 2:
        pegx = -110
    elif col == 3:
        pegx = -20
    elif col == 4:
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
    else:
        fillcolor("white")
        pencolor("white")
    penup()
    goto(pegx,pegy)
    pendown()
    begin_fill()
    circle(20,360)
    end_fill()

