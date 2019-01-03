from map import Map
from Algorithms import *
print("enter height and width")
height = int(input())
width = int(input())
print("goal index")
x = int(input())
y = int(input())
goal = (x,y)
print("player Location")
x = int(input())
y = int(input())
playerLocation = (x,y)
map = Map(height,width,goal,playerLocation)
map.place()
map.getPossibleMoves()
s = input()
if s == "die":
    die = someAlgorithm()
    die.apply(map)

