import Heuristics as heuristics

def execute(initialState, objective, heuristic):
    print("Experimento 2\n")

    if heuristic == 1:
        path, generatedNodes, time = heuristics.tryAStar(initialState, objective, heuristics.countElementsWrongPlaceH1)
        
        print("Heurística h1:")
        print("Valor:", heuristics.getH1Value(initialState, objective))
        print("Caminho:", path)
        print("Nós gerados:", generatedNodes)
        print("Tempo:", time, "segundos")

    if heuristic == 2:
        path, generatedNodes, time = heuristics.tryAStar(initialState, objective, heuristics.calcManhattanDistanceH2)
        
        print("\nHeurística h2:")
        print("Valor:", heuristics.getH2Value(initialState, objective))
        print("Caminho:", path)
        print("Nós gerados:", generatedNodes)
        print("Tempo:", time, "segundos")
