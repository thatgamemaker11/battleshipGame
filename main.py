
from turtle import*
import art
import board
import numtolet
import peg
import ship

board.board()

#list = ship.posgen()
list = ['d', 1, 'd', 2, 'd', 3]
print(list)
ship.shipdraw(list)

hit = 0
miss = 0
loop = 0
tmephit = 2
while loop == 0:
    while True:
        numbers = [1, 2, 3, 4, 5]
        snumbers = ["1", "2", "3", "4", "5"]
        letters = ["a", "b", "c", "d", "e"]
        print("=============================================")
        col = input("what column would you like to try?")


        if col not in letters:
            print("Not a letter (A-e)")
        else:
            row = input("what Row? would you like to try?")
            print("=============================================")
            if row not in snumbers:
                print("Not a number")
            else:
                break
                loop = 1
    row = int(row)

    #=========================================


    if miss == 6:
        clear()
        print("you loose")
        art.lose()

    elif hit == 2:
        clear()
        print("you win!!!")
        art.win()

    else:



        if list[0] == col and list[1] == row:
            print("hit")
            hit = hit+1
            temphit = 1
        elif list[2] == col and list[3] == row:
            print("hit")
            hit = hit + 1
            temphit = 1
        elif list[4] == col and list[5] == row:
            print("hit")
            hit = hit + 1
            temphit = 1
        else:
            print("miss")
            miss = miss + 1





        peg.peg(col,row,tmephit)

        print(tmephit)
        print(hit)
        print(miss)
        print(col,row)
        temphit = 2

input()

