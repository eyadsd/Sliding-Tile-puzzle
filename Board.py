import numpy
import copy
class Board:
    "this class represents the Board as a 2D array"

    pieces = {}
    
        
    def __init__(self,height, width):
        self.boardHeight = int(height)
        self.boardWidth = int(width)
        self.tileArray = []
        

        self.tileArray = numpy.zeros((self.boardHeight, self.boardWidth))

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
                self.tileArray[i][j] = int(input())
                id = self.tileArray[i][j]
                if(id != 0):
                    if(id in self.pieces):
                        piece = self.pieces[id]
                        piece.append((i,j))

                    else:
                        self.pieces[id] = []
                        self.pieces[id].append((i,j))

               
                
         
        print(self.tileArray)
        print(self.pieces)
        for key, value in self.pieces.items():
            print(key, "  ", value)
        print("selelected object:")
        self.selectedPiece = int(input())
        print("desired location")
        x = int(input())
        y = int(input())
        self.selectedLocation = (x,y)

    def movePiece(self,pieceKey, direction):
        "move a piece in a certain direction"
        piece = self.pieces[pieceKey]
        if (self.isMovable(pieceKey,direction)):
            for coord in piece:
                i = coord[0]
                j = coord[1]
                self.tileArray[i][j] = 0

            for idx in range(len(piece)):
                coord = piece[idx]
                i = coord[0]
                j = coord[1]
                if direction == "left":
                    self.tileArray[i][j-1] = pieceKey
                    piece[idx] = (i,j-1)
                    

                elif direction == "right":
                    self.tileArray[i][j+1] = pieceKey
                    piece[idx] = (i,j+1)


                elif direction == "up":
                    self.tileArray[i-1][j] = pieceKey
                    piece[idx] = (i-1,j)


                elif direction == "down":
                    self.tileArray[i+1][j] = pieceKey
                    piece[idx] = (i+1,j)


                else:
                    print("input error !")
                    
            
        
                


    def isMovable(self,pieceKey, direction):
        "check if the selectd piece is movable in a certain direction"
        piece = self.pieces[pieceKey]
        try: 
            for coord in piece:
                i = coord[0]
                j = coord[1]
                
                if direction == "left":
                    if self.tileArray[i][j-1] != 0 and self.tileArray[i][j-1] != pieceKey or j-1<0:
                        return 0

                elif direction == "right":
                    if self.tileArray[i][j+1] != 0 and self.tileArray[i][j+1] != pieceKey or j+1<0:
                        return 0

                elif direction == "up":
                    if self.tileArray[i-1][j] != 0 and self.tileArray[i-1][j] != pieceKey or i-1<0:
                        return 0

                elif direction == "down":
                    if self.tileArray[i+1][j] != 0 and self.tileArray[i+1][j] != pieceKey or i+1<0:
                        return 0

                else:
                    print("input error !")
                    return 0

            
            return 1
        except IndexError:
            return 0
    
    def getPossibleMoves(self):
        possibleMoves = []
        for key in self.pieces:
            if self.isMovable(key,"up"):
                state = copy.deepcopy(self)
                state.pieces = copy.deepcopy(self.pieces)
                state.movePiece(key,"up")
                possibleMoves.append(state)
                print(state.tileArray)
            if self.isMovable(key,"down"):
                state = copy.deepcopy(self)
                state.pieces = copy.deepcopy(self.pieces)
                state.movePiece(key,"down")
                possibleMoves.append(state)
                print(state.tileArray)
            if self.isMovable(key,"left"):
                state = copy.deepcopy(self)
                state.pieces = copy.deepcopy(self.pieces)
                state.movePiece(key,"left")
                possibleMoves.append(state)
                print(state.tileArray)
            if self.isMovable(key,"right"):
                state = copy.deepcopy(self)
                state.pieces = copy.deepcopy(self.pieces)
                state.movePiece(key,"right")
                possibleMoves.append(state)
                print(state.tileArray)
        return possibleMoves

    def checkWin(self):
        l = self.pieces[self.selectedPiece]
        for coords in l:
            if coords == self.selectedLocation:
                return 1
        return 0
    def manhattanDistance(self):
        coords = self.pieces[self.selectedPiece]
        min = 9999999
        for coord in coords:
            distance = (self.selectedLocation[0] - coord[0]) + (self.selectedLocation[1] - coord[1])
            if distance < min:
                min = distance

        return min
