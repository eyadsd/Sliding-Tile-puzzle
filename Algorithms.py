from collections import deque
from heapq import *
class DFS:
    
    def __init__(self):
        self.stack = []
        self.visited = {}
    def dfsRecursive(self,state):
        self.visited[hash(str(state.tileArray))] = 1
        l = state.getPossibleMoves()
        for v in l:
            if not (hash(str(v.tileArray)) in self.visited):
                self.visited[hash(str(v.tileArray))] = 1
                print(state.tileArray)
                if state.checkWin() == 1:
                    print("win")
                    return 
                self.dfsRecursive(v)

class BFS:
    def __init__(self):
        self.queue = deque([])
        self.visited = {}
    def bfs(self,state):
        self.queue.append(state)
        self.visited[hash(str(state.tileArray))] = 1
        while(self.queue):
            v = self.queue.popleft()
            print(v.tileArray)
            if v.checkWin() == 1:
                print("win!")
                return 
            l = v.getPossibleMoves()
            for w in l:
                if not (hash(str(w.tileArray)) in self.visited):
                    self.queue.append(w)
                    self.visited[hash(str(w.tileArray))] = 1
class someAlgorithm:
    def __init__(self):
        self.heapCount = 0
        self.heap = []
        self.visited = {}
        self.distanceFromRoot = {}
    def apply(self, state):
        count = 0
        self.distanceFromRoot[state] = 0
        heappush(self.heap,(state.manhattanDistance() + self.distanceFromRoot[state],self.heapCount,state))
        self.heapCount += 1
        self.visited[hash(str(state.tileArray))] = 1
        while(self.heap):
            t = heappop(self.heap)
            v = t[2]
            print(v.tileArray)
            #v.print()
            if v.checkWin() == 1:
                print("win!")
                print(self.distanceFromRoot[v])
                print(count)
                return 
            l = v.getPossibleMoves()
            for w in l:
                if not (hash(str(w.tileArray)) in self.visited):
                    count = count + 1
                    self.distanceFromRoot[w] = self.distanceFromRoot[v] + 1
                    heappush(self.heap,(w.manhattanDistance() + self.distanceFromRoot[state],self.heapCount,w))
                    self.heapCount += 1
                    self.visited[hash(str(w.tileArray))] = 1
