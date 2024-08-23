def experiment_1():
    #[
    #    i0  i1  i2
    #    i3  i4  i5
    #    i7  i8  i9
    #]
    initialState = [
        [2, 8, 3],
        [1, 6, 4],
        [0, 7, 5]
    ];

    objective = [
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ];

    heuristic = countElementsWrongPosition(initialState, objective)
    depth = 0;

    opened = [initialState];
    closed = [];

    while not is_empty(opened):
        X = initialState


        closed.append(X)

def countElementsWrongPosition(matrix, objective):
    wrongCounter = 0
    
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if matrix[i][j] != objective[i][j]:
                wrongCounter += 1

    return wrongCounter-1 # 0 do not count

def is_empty(matrix):
    for row in matrix:
        for element in row:
            if element is not None:
                return False
    return True