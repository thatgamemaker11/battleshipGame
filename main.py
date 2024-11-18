import board
import peg
import ship

board.board()
peg.peg(5,1,1)
peg.peg(4,2,0)
peg.peg(3,3,1)
peg.peg(2,4,0)
peg.peg(1,5,1)

#list = ["a",2,"a",3,"a",4]
list = ship.posgen()
ship.shipdraw(list)





input()

