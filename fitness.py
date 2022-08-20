
import numpy as np
import check_solution as CheckSolution
from cmath import inf


def verify(setCoveringProblem, sol):
    cost = setCoveringProblem["coverageCostVector"]
    feasible = CheckSolution.verify(setCoveringProblem, sol)[0]
    if not feasible:
        return inf
    else:
        fitness = np.dot(sol, cost)
        return fitness
