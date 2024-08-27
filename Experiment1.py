import Heuristics as heuristics

def execute(initialState, objective, heuristic):
    print("Experimento 1\n")

    if heuristic == 1:
        path_ex1_h1, nodes_generated_ex1_h1, time_ex1_h1 = heuristics.tryAStar(initialState, objective, heuristics.countElementsWrongPlaceH1)
        
        print("Heurística h1:")
        print("Valor:", heuristics.getH1Value(initialState, objective))
        print("Caminho:", path_ex1_h1)
        print("Nós gerados:", nodes_generated_ex1_h1)
        print("Tempo:", time_ex1_h1, "segundos")

    if heuristic == 2:
        path, generatedNodes, time = heuristics.tryAStar(initialState, objective, heuristics.calcManhattanDistanceH2)
        
        print("\nHeurística h2:")
        print("Valor:", heuristics.getH2Value(initialState, objective))
        print("Caminho:", path)
        print("Nós gerados:", generatedNodes)
        print("Tempo:", time, "segundos")