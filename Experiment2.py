import Heuristics as heuristics

def execute(initialState, objective, heuristic):
    print("Experiment 2\n")

    if heuristic == 1:
        path, generatedNodes, time = heuristics.tryAStar(initialState, objective, heuristics.countElementsWrongPlaceH1)
        
        print("H1:")
        print("Value:", heuristics.getH1Value(initialState, objective))
        print("Path:", path)
        print("Generated nodes:", generatedNodes)
        print("Time:", time, "seconds")

    if heuristic == 2:
        path, generatedNodes, time = heuristics.tryAStar(initialState, objective, heuristics.calcManhattanDistanceH2)
        
        print("\nH2:")
        print("Value:", heuristics.getH2Value(initialState, objective))
        print("Path:", path)
        print("Generated nodes:", generatedNodes)
        print("Time:", time, "seconds")
