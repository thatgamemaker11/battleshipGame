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




    penup()
    pencolor("white")
    fillcolor("white")
    goto(pegx,0)
    pendown()
    begin_fill()
    circle(20,360)
    end_fill()
