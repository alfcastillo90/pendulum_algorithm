
import numpy as np
import check_solution as CheckSolution

def complex(setCoveringProblem, solution):
    sol =  np.reshape(solution, (setCoveringProblem["columns"],))
    set = setCoveringProblem["coverageMatrix"]
    
    feasible, aux = CheckSolution.verify(setCoveringProblem,sol)

    while not feasible:
        notCoveredRestrictions = np.zeros((setCoveringProblem["rows"],))
        notCoveredRestrictions[np.argwhere(aux == 0)] = 1           # Vector indica las restricciones no cubiertas
        cnc = np.dot(notCoveredRestrictions, set)                   # Cantidad de restricciones no cubiertas que cubre cada columna (de tamaño n)
        trade_off = np.divide(setCoveringProblem["coverageCostVector"],cnc)               # Trade off entre zonas no cubiertas y costo de seleccionar cada columna
        idx = np.argmin(trade_off)                          # Selecciono la columna con el trade off mas bajo
        sol[idx] = 1                                        # Asigno 1 a esa columna
        feasible, aux = CheckSolution.verify(setCoveringProblem,sol)               # Verifico si la solucion actualizada es factible

    return sol