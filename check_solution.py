import numpy as np

def verify(setCoveringProblem, solution):
    flag = True
    set = setCoveringProblem["coverageMatrix"]
    multiplyMatrix = np.dot(set,solution)

    if 0 in multiplyMatrix:                    
        flag = False

    return flag, multiplyMatrix