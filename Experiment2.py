import Heuristics as heuristics

def execute(initialState, objective, heuristic):
    print("Experiment 2\n")

    if heuristic == 1:
        path, generatedNodes, time = heuristics.tryAStar(initialState, objective)
        
        print("H1:")
        print("Path:", path)
        print("Generated nodes:", generatedNodes)
        print("Time:", time, "seconds")

    if heuristic == 2:
        path, generatedNodes, time = heuristics.tryAStar(initialState, objective)
        
        print("\nH2:")
        print("Path:", path)
        print("Generated nodes:", generatedNodes)
        print("Time:", time, "seconds")
