import board
import peg
import ship

board.board()
peg.peg(5,1,1)
peg.peg(4,2,0)
peg.peg(3,3,1)
peg.peg(2,4,0)
peg.peg(1,5,1)

pos = ship.posgen()

ship.shipPos(pos)
pos[1] = pos[1] + 1
ship.shipPos(pos)
pos[1] = pos[1] - 2
ship.shipPos(pos)

print(pos)




input()

