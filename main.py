import time
from heapq import heappush, heappop
import pandas as pd
from IPython.display import display

# Função de heurística h1: Contagem de peças fora do lugar
def h1(state, objective):
    return sum(1 for i, value in enumerate(state) if value != 0 and value != objective[i])

# Função de heurística h2: Soma das distâncias de Manhattan
def h2(state, objective):
    boardSize = int(len(state) ** 0.5)
    distance = 0
    for i, value in enumerate(state):
        if value != 0:
            targetIndex = objective.index(value)
            x1, y1 = i // boardSize, i % boardSize
            x2, y2 = targetIndex // boardSize, targetIndex % boardSize
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

# Função para gerar os filhos do estado atual
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

# Função para o algoritmo A* com o cálculo de f(n) = g(n) + h(n)
def tryAStar(initialState, objective, heuristic):
    initialTime = time.time()
    openedList = []
    heappush(openedList, (heuristic(initialState, objective), 0, initialState, []))  # (f, g, estado, caminho)
    closed = set()
    generatedNodes = 0
    goal_g_value = None

    while openedList:
        f, g, actual, path = heappop(openedList)
        if actual == objective:
            finalTime = time.time()
            goal_g_value = g
            return path + [actual], generatedNodes, finalTime - initialTime, goal_g_value
        closed.add(actual)
        generatedNodes += 1
        for filho in generateChildren(actual):
            if filho not in closed:
                new_g = g + 1
                new_f = new_g + heuristic(filho, objective)
                heappush(openedList, (new_f, new_g, filho, path + [actual]))
    return None, generatedNodes, None, None

# Variáveis globais para armazenar resultados dos experimentos
nodes_generated_ex1_h1 = nodes_generated_ex2_h1 = 0
time_ex1_h1 = time_ex2_h1 = 0
g_value_ex1_h1 = g_value_ex2_h1 = 0
nodes_generated_ex1_h2 = nodes_generated_ex2_h2 = 0
time_ex1_h2 = time_ex2_h2 = 0
g_value_ex1_h2 = g_value_ex2_h2 = 0

def execute_experiment1(initialState, objective, heuristic):
    global nodes_generated_ex1_h1, nodes_generated_ex1_h2, time_ex1_h1, time_ex1_h2
    global g_value_ex1_h1, g_value_ex1_h2
    print("\nExperiment 1")
    path, generatedNodes, elapsedTime, goal_g_value = tryAStar(initialState, objective, heuristic)
    if heuristic == h1:
        print("H1:")
        nodes_generated_ex1_h1 = generatedNodes
        time_ex1_h1 = elapsedTime
        g_value_ex1_h1 = goal_g_value
    elif heuristic == h2:
        print("\nH2:")
        nodes_generated_ex1_h2 = generatedNodes
        time_ex1_h2 = elapsedTime
        g_value_ex1_h2 = goal_g_value
    print("Path:", path)
    print("Generated nodes:", generatedNodes)
    print("Time:", elapsedTime, "seconds")
    print("Value of g(n) at goal:", goal_g_value)

def execute_experiment2(initialState, objective, heuristic):
    global nodes_generated_ex2_h1, nodes_generated_ex2_h2, time_ex2_h1, time_ex2_h2
    global g_value_ex2_h1, g_value_ex2_h2
    print("\nExperiment 2")
    path, generatedNodes, elapsedTime, goal_g_value = tryAStar(initialState, objective, heuristic)
    if heuristic == h1:
        print("H1:")
        nodes_generated_ex2_h1 = generatedNodes
        time_ex2_h1 = elapsedTime
        g_value_ex2_h1 = goal_g_value
    elif heuristic == h2:
        print("\nH2:")
        nodes_generated_ex2_h2 = generatedNodes
        time_ex2_h2 = elapsedTime
        g_value_ex2_h2 = goal_g_value
    print("Path:", path)
    print("Generated nodes:", generatedNodes)
    print("Time:", elapsedTime, "seconds")
    print("Value of g(n) at goal:", goal_g_value)

# Função para criar e exibir a tabela comparativa
def plot_experiment_results():
    # Dados dos experimentos
    data = {
        "Experimento": ["Exp1", "Exp2"],
        "h1(n) - Nós gerados": [nodes_generated_ex1_h1, nodes_generated_ex2_h1],
        "h1(n) - Tempo (s)": [time_ex1_h1, time_ex2_h1],
        "h1(n) - Valor de g(n)": [g_value_ex1_h1, g_value_ex2_h1],
        "h2(n) - Nós gerados": [nodes_generated_ex1_h2, nodes_generated_ex2_h2],
        "h2(n) - Tempo (s)": [time_ex1_h2, time_ex2_h2],
        "h2(n) - Valor de g(n)": [g_value_ex1_h2, g_value_ex2_h2],
    }

    # Criando o DataFrame
    df = pd.DataFrame(data)

    # Definindo o índice do DataFrame como a coluna "Experimento"
    df.set_index("Experimento", inplace=True)

    # Estilizando o DataFrame para se parecer com uma planilha do Excel
    styled_df = df.style \
        .background_gradient(cmap="Greys", low=0, high=1) \
        .format({
            'h1(n) - Tempo (s)': '{:.10f}',  # Ajuste o número de casas decimais conforme necessário
            'h2(n) - Tempo (s)': '{:.10f}',
            'h1(n) - Valor de g(n)': '{:.0f}',
            'h2(n) - Valor de g(n)': '{:.0f}'
        })  \
        .set_table_styles({
            'Experimento': [{'selector': 'td:hover', 'props': 'background-color: #f5f5f5;'}],
            '': [{'selector': 'th', 'props': 'background-color: #d3d3d3; border: 1px solid black;'}],
            'td': [{'selector': 'td', 'props': 'border: 1px solid black;'}]
        }) \
        .set_caption("Comparação dos Resultados dos Experimentos")

    # Exibindo o DataFrame estilizado
    display(styled_df)

# Configuração dos experimentos
initialState1 = (2, 8, 3, 1, 6, 4, 0, 7, 5)
objective1 = (1, 2, 3, 8, 0, 4, 7, 6, 5)

initialState2 = (7, 2, 4, 5, 0, 6, 8, 3, 1)
objective2 = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Executando os experimentos
execute_experiment1(initialState1, objective1, h1)
execute_experiment1(initialState1, objective1, h2)
execute_experiment2(initialState2, objective2, h1)
execute_experiment2(initialState2, objective2, h2)

# Plotando os resultados
plot_experiment_results()