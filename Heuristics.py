import time
from heapq import heappush, heappop

def getH1Value(state, goal):
    return sum(1 for i in range(len(state)) if state[i] != 0 and state[i] != goal[i])

def getH2Value(state, goal):
    distance = 0
    n = int(len(state) ** 0.5)

    for i in range(len(state)):
        if state[i] != 0:
            x1, y1 = i // n, i % n
            x2, y2 = goal.index(state[i]) // n, goal.index(state[i]) % n
            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance

def countElementsWrongPlaceH1(actual, objective):
    counter = 0
    for i in range(len(actual)):
        if actual[i] != 0 and actual[i] != objective[i]:
            counter += 1
    return counter

def calcManhattanDistanceH2(actual, objective):
    totalDistance = 0
    boardSize = int(len(actual) ** 0.5)

    for i in range(len(actual)):
        if actual[i] != 0:
            x1, y1 = i // boardSize, i % boardSize
            x2, y2 = objective.index(actual[i]) // boardSize, objective.index(actual[i]) % boardSize

            totalDistance += abs(x1 - x2) + abs(y1 - y2) 

    return totalDistance

def generateChildren(actual):
    boardSize = int(len(actual) ** 0.5) 

    whiteIndex = actual.index(0)

    x, y = whiteIndex // boardSize, whiteIndex % boardSize
    children = []
    
    movs = [(-1, 0), (1, 0), (0, -1), (0, 1)]   

    for mov in movs:
        newX, newY = x + mov[0], y + mov[1]
        
        if 0 <= newX < boardSize and 0 <= newY < boardSize:
            newWhiteIndex = newX * boardSize + newY
            
            newState = list(actual)
            newState[whiteIndex], newState[newWhiteIndex] = newState[newWhiteIndex], newState[whiteIndex]

            children.append(tuple(newState))

    return children

def tryAStar(initialState, objective, heuristic):
    initialTime = time.time()
    openedList = []
    
    heappush(openedList, (0 + heuristic(initialState, objective), 0, initialState, []))

    closed = set()

    generatedNodes = 0

    while openedList:
        _, g, actual, path = heappop(openedList)

        if actual == objective:
            finalTime = time.time()
            return path + [actual], generatedNodes, finalTime - initialTime

        closed.add(actual)
        generatedNodes += 1

        for filho in generateChildren(actual):
            if filho not in closed:
                novo_g = g + 1
                heappush(openedList, (novo_g + heuristic(filho, objective), novo_g, filho, path + [actual]))

    return None, generatedNodes, None
