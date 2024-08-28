import Experiment1 as ex1
import Experiment2 as ex2

initialState = (2, 8, 3, 1, 6, 4, 0, 7, 5)
objective = (1, 2, 3, 8, 0, 4, 7, 6, 5)

ex1.execute(initialState, objective, 1)
ex1.execute(initialState, objective, 2)

initialState = (7, 2, 4, 5, 0, 6, 8, 3, 1)
objective = (1, 2, 3, 4, 5, 6, 7, 8, 0)

ex2.execute(initialState, objective, 1)
ex2.execute(initialState, objective, 2)