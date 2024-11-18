import board
import peg
import randship

board.board()
peg.peg(5,1,1)
peg.peg(4,2,0)
peg.peg(3,3,1)
peg.peg(2,4,0)
peg.peg(1,5,1)

shipos = randship.posgen()
peg.shipPos(shipos)
peg.shipPos(shipos +1)
peg.shipPos(shipos +2)



input()

