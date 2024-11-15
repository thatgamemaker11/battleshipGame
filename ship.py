import random
from turtle import *
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
def posgen():
    xpos = random.randint(1,5)
    ypos = random.randint(1,5)

    poslist = [xpos,ypos]
    return poslist
