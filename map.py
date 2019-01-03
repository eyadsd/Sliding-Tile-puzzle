import numpy as np
import copy
class Map:

    def __init__(self,height, width,goal = (0,0),playerLocation = (0,0)):
        self.boardHeight = int(height)
        self.boardWidth = int(width)
        self.tileArray = []
        for i in range(height):
            self.tileArray.append([])
            for j in range(width):
                self.tileArray[i].append (-1)

        self.weights = {"m": 100,"s":30,"p":10}
        self.playerLocation = playerLocation
        self.goal = goal
    def __hash__(self):
        l = []
        for i in range(self.boardHeight):
            for j in range(self.boardWidth):
                l.append(self.tileArray[i][j])
        t = tuple(l)
        return hash(t)

    def place(self):
        "place the pieces"
        for i in range(self.boardHeight):
            for j in range(self.boardWidth):
                print(i ," " , j, "=")
                self.tileArray[i][j] = input()

    def move(self,direction):
        x,y = self.playerLocation
        if direction == "up":
            self.playerLocation = (x,y-1)
        if direction == "down":
            self.playerLocation = (x,y+1)
        if direction == "left":
            self.playerLocation = (x -1,y)
        if direction == "right":
            self.playerLocation = (x+1,y)
    def print(self):
        
        for i in range(self.boardHeight):
            for j in range(self.boardWidth):
                currentLocation = (i,j)
                if currentLocation == self.playerLocation:
                    print("H", end = " ")
                else:
                    print(self.tileArray[i][j], end =" ")
                
            print()


    def getPossibleMoves(self):
        possibleMoves = []
    
        if self.isMovable("up"):
            state = copy.deepcopy(self)
            state.move("up")
            possibleMoves.append(state)
            #self.print()
        if self.isMovable("down"):
            state = copy.deepcopy(self)
            state.move("down")
            possibleMoves.append(state)
            #self.print()
        if self.isMovable("left"):
            state = copy.deepcopy(self)
            state.move("left")
            possibleMoves.append(state)
            #self.print()
        if self.isMovable("right"):
            state = copy.deepcopy(self)
            state.move("right")
            possibleMoves.append(state)
            #self.print()
        return possibleMoves

    def checkWin(self):
        if  self.playerLocation == self.goal:
            return 1
        else: 
            return 0

    def isMovable(self,direction):
        x,y = self.playerLocation
        try:
            if direction == "up":
                if self.tileArray[x][y-1] == "w":
                    return 0
            if direction == "down":
                if self.tileArray[x][y+1] == "w":
                    return 0

            if direction == "left":
                if self.tileArray[x-1][y] == "w":
                    return 0
            if direction == "right":
                if self.tileArray[x+1][y] == "w":
                    return 0
        except IndexError:
            return 0

        return 1

    def manhattanDistance(self):
        x,y = self.playerLocation       
        distance = (self.goal[0] - x) + (self.goal[1] - y)
        return distance
        


