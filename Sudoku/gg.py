from random import sample
from random import *
# num=[5,1,3,2]
# s=[sum(num[0:index+1]) for index,x in enumerate(num)]
# print(s)

base  = 3
side  = base*base

# pattern for a baseline valid solution
def pattern(r,c): return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): return sample(s,len(s))
rBase = range(base)
rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ]
cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
nums  = shuffle(range(1,base*base+1))

# produce board using randomized baseline pattern
board = [[nums[pattern(r,c)] for c in cols] for r in rows ]
print(board)

squares = side*side
empties = squares * 3//4
a = board
for p in sample(range(squares),empties):
    # print(p)
    # print(p//side)
    # print(p%side)
    a[p//side][p%side] = 0
print(a)
print(a[0][0])
# for line in board: print("["+"  ".join(f"{n or '.':{numSize}}" for n in line)+"]")




# def expandLine(line):
#     return line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:13]
# line0  = expandLine("╔═══╤═══╦═══╗")
# line1  = expandLine("║ . │ . ║ . ║")
# line2  = expandLine("╟───┼───╫───╢")
# line3  = expandLine("╠═══╪═══╬═══╣")
# line4  = expandLine("╚═══╧═══╩═══╝")
#
# symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# nums   = [ [""]+[symbol[n] for n in row] for row in board ]
# print(line0)
# for r in range(1,side+1):
#     print( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
#     print([line2,line3,line4][(r%side==0)+(r%base==0)])

