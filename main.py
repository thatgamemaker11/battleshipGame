import board
import peg
import ship

board.board()

list = ship.posgen()
print(list)
ship.shipdraw(list)


print("=============================================")
col = input("what column would you like to try?")
row = input("what Row? would you like to try?")
print("=============================================")

row = int(row)

numbers = [1, 2, 3, 4, 5]
letters = ["a", "b", "c", "d", "e"]

if col in letters:
    print("not a letter") #######fix


if row in numbers:
    print("not a number")


peg.peg(col,row,1)








input()

