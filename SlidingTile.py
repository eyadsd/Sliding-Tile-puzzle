from Board import Board
import numpy
from Algorithms import *
print("welcome to sliding tile puzzle")
a = numpy.zeros((5,5))
b = tuple(a)
print(b)
l = []
l.append((1,2))
l.append((3,2))
print(l[0])
t = l[0]
print(t[0])
print(t[1])

height = input()
width = input()
board = Board(height,width)

board.place()
'''print("bfs:\n")
bfs = BFS()
bfs.bfs(board)

print("dfs:\n")
dfs =  DFS()
dfs.dfsRecursive(board)'''
##board.getPossibleMoves()
dfs = DFS()
while 1:
    print("manhattan distance = ", board.manhattanDistance())
    s = input()
    if s == "dfs":
        dfs = DFS()
        dfs.dfsRecursive(board)
    if s == "bfs":
        bfs = BFS()
        bfs.bfs(board)
    if (s == "move"):
        print ("input direction ")
        direction = input()
        print("input key")
        key = int(input())
        board.movePiece(key,direction)
        print(board.tileArray)
        if(board.checkWin() == 1):
            print("win!")
    if s == "die":
        die = someAlgorithm()
        die.apply(board)
