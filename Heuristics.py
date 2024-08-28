import time
from heapq import heappush, heappop

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

def tryAStar(initialState, objective):
    initialTime = time.time()
    openedList = []
    
    # Aqui, o primeiro elemento da tupla é apenas o valor de g(n) (custo)
    heappush(openedList, (0, initialState, []))

    closed = set()

    generatedNodes = 0

    while openedList:
        g, actual, path = heappop(openedList)

        if actual == objective:
            finalTime = time.time()
            return path + [actual], generatedNodes, finalTime - initialTime

        closed.add(actual)
        generatedNodes += 1

        for filho in generateChildren(actual):
            if filho not in closed:
                novo_g = g + 1
                heappush(openedList, (novo_g, filho, path + [actual]))

    return None, generatedNodes, None
