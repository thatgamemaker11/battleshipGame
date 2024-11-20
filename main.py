import board
import numtolet
import peg
import ship

board.board()

#list = ship.posgen()
list = ['c', 1, 'c', 2, 'c', 3]
print(list)
ship.shipdraw(list)


print("=============================================")
col = input("what column would you like to try?")
row = input("what Row? would you like to try?")
print("=============================================")

row = int(row)
#col = numtolet.translet(col)

numbers = [1, 2, 3, 4, 5]
letters = ["a", "b", "c", "d", "e"]

# if col not in numbers:
#     print("not a letter")
#
# if row not in letters:
#     print("not a number")
#=========================================

# hits = 0
# letcol = col
# letcol = numtolet.transnum(letcol)
# checkrow = row
# print(letcol)
# print(checkrow)
# if list[0] == letcol and list[1] == row:
#     print("hit")
# elif list[2] == letcol and list[3] == row:
#     print("hit")
# elif list[4] == letcol and list[5] == row:
#     print("hit")
# else:
#     print("miss")




peg.peg(col,row,1)
print(col,row)

input()

