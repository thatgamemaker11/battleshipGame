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
def shipdraw(shiplist):
    num1 = shiplist[1]
    num2 = shiplist[3]
    num3 = shiplist[5]

    if shiplist[0] == "a":
        pos1 = 1
    elif shiplist[0] == "b":
        pos1 = 2
    elif shiplist[0] == "c":
        pos1 = 3
    elif shiplist[0] == "d":
        pos1 = 4
    elif shiplist[0] == "e":
        pos1 = 5
    else:
        pos1 = 1
#=============================
    if shiplist[2] == "a":
        pos2 = 1
    elif shiplist[2]  == "b":
        pos2 = 2
    elif shiplist[2]  == "c":
        pos2 = 3
    elif shiplist[2]  == "d":
        pos2 = 4
    elif shiplist[2]  == "e":
        pos2 = 5
    else:
        pos2 = 1
#=============================
    if shiplist[4]  == "a":
        pos3 = 1
    elif shiplist[4] == "b":
        pos3 = 2
    elif shiplist[4] == "c":
        pos3 = 3
    elif shiplist[4] == "d":
        pos3 = 4
    elif shiplist[4] == "e":
        pos3 = 5
    else:
        pos3 = 1

    shipPos([pos1, num1])
    shipPos([pos2, num2])
    shipPos([pos3, num3])
