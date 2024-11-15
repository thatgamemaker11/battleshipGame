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
        pegy = -180
    elif row == 2:
        pegy = -90
    elif row == 3:
        pegy = 0
    elif row == 4:
        pegy = 90
    else:
        pegy = 180

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


def shipPos(pos):
    shipcol = pos[0]
    shiprow = pos[1]

    if shipcol == 1:
        shippegx = -200
    elif shipcol == 2:
        shippegx = -110
    elif shipcol == 3:
        shippegx = -20
    elif shipcol == 4:
        shippegx = 70
    else:
        shippegx = 160
    # ============================
    if shiprow == 1:
        shippegy = -180
    elif shiprow == 2:
        shippegy = -90
    elif shiprow == 3:
        shippegy = 0
    elif shiprow == 4:
        shippegy = 90
    else:
        shippegy = 180



    penup()
    pencolor("grey")
    fillcolor("grey")
    goto(shippegx,shippegy)
    pendown()
    begin_fill()
    circle(20,360)
    end_fill()
